/**
 * VSTEP B2 MASTER LEARNING PORTAL - MAIN APPLICATION CONTROLLER
 * Styled for Whitepace - SaaS Landing Page Layout
 */

(function () {
  'use strict';

  // Application State
  const state = {
    currentStudioTab: 'reader',
    activeFile: null,
    readerFontSize: 16,
    
    // Flashcard State
    fcDeckFilter: 'all',
    fcList: [],
    fcIndex: 0,
    fcFlipped: false,
    fcStreak: parseInt(localStorage.getItem('vstep_fc_streak') || '0', 10),
    fcMastered: JSON.parse(localStorage.getItem('vstep_fc_mastered') || '[]'),
    
    // Quiz State
    quizIndex: 0,
    quizScore: 0,
    quizAnswered: false,
    
    // Checklist State
    checklist: JSON.parse(localStorage.getItem('vstep_checklist') || '{}')
  };

  const elements = {};

  function init() {
    if (!window.KB_DATA) {
      console.error('KB_DATA is missing!');
      return;
    }

    cacheDOMElements();
    setupNavigation();
    setupStudioTabs();
    setupGlobalSearch();
    renderSidebarFiles();
    renderGrammarHub();
    renderVocabHub();
    initFlashcards();
    initQuiz();
    initChecklist();

    // Default open first file
    if (window.KB_DATA.modules.length > 0 && window.KB_DATA.modules[0].files.length > 0) {
      state.activeFile = window.KB_DATA.modules[0].files[0];
      renderFileContent(state.activeFile);
    }

    document.addEventListener('keydown', handleGlobalKeydown);
  }

  function cacheDOMElements() {
    elements.searchTriggerBtn = document.getElementById('searchTriggerBtn');
    elements.searchModal = document.getElementById('searchModal');
    elements.modalSearchInput = document.getElementById('modalSearchInput');
    elements.searchResultsList = document.getElementById('searchResultsList');
    elements.modalCloseBtn = document.getElementById('modalCloseBtn');
    
    // Studio Panels
    elements.studioPanels = {
      reader: document.getElementById('studio-panel-reader'),
      grammar: document.getElementById('studio-panel-grammar'),
      vocab: document.getElementById('studio-panel-vocab'),
      flashcards: document.getElementById('studio-panel-flashcards'),
      quiz: document.getElementById('studio-panel-quiz'),
      checklist: document.getElementById('studio-panel-checklist')
    };

    elements.studioTabBtns = document.querySelectorAll('.studio-tab-btn');
    
    // Reader Elements
    elements.readerSidebar = document.getElementById('readerSidebar');
    elements.readerContent = document.getElementById('readerContent');
    elements.readerTitle = document.getElementById('readerTitle');
    elements.sidebarSearch = document.getElementById('sidebarSearch');
    
    // Flashcard Elements
    elements.fcCard = document.getElementById('fcCard');
    elements.fcFront = document.getElementById('fcFront');
    elements.fcBack = document.getElementById('fcBack');
    elements.fcCategory = document.getElementById('fcCategory');
    elements.fcCounter = document.getElementById('fcCounter');
    elements.fcStreak = document.getElementById('fcStreak');
    elements.fcBtnAgain = document.getElementById('fcBtnAgain');
    elements.fcBtnGood = document.getElementById('fcBtnGood');
    elements.fcAudioBtn = document.getElementById('fcAudioBtn');
    elements.deckButtons = document.querySelectorAll('.deck-btn');

    // Hero Preview Card
    elements.heroFcWord = document.getElementById('heroFcWord');
    elements.heroFcAudio = document.getElementById('heroFcAudio');
    
    // Quiz Elements
    elements.quizCategory = document.getElementById('quizCategory');
    elements.quizQuestion = document.getElementById('quizQuestion');
    elements.quizOptions = document.getElementById('quizOptions');
    elements.quizExplanation = document.getElementById('quizExplanation');
    elements.quizProgress = document.getElementById('quizProgress');
    elements.quizNextBtn = document.getElementById('quizNextBtn');
    
    // Checklist Elements
    elements.checklistBody = document.getElementById('checklistBody');
    elements.readinessPercent = document.getElementById('readinessPercent');
    elements.readinessProgressBar = document.getElementById('readinessProgressBar');
    elements.heroReadiness = document.getElementById('heroReadiness');
  }

  // Navigation Links
  function setupNavigation() {
    document.querySelectorAll('[data-target-studio]').forEach(el => {
      el.addEventListener('click', (e) => {
        e.preventDefault();
        const tab = el.getAttribute('data-target-studio');
        switchStudioTab(tab);
        const studioEl = document.getElementById('learning-studio');
        if (studioEl) {
          studioEl.scrollIntoView({ behavior: 'smooth' });
        }
      });
    });
  }

  // Studio Tabs
  function setupStudioTabs() {
    elements.studioTabBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const tabName = btn.getAttribute('data-tab');
        switchStudioTab(tabName);
      });
    });
  }

  function switchStudioTab(tabName) {
    if (!elements.studioPanels[tabName]) return;
    state.currentStudioTab = tabName;

    elements.studioTabBtns.forEach(b => {
      b.classList.toggle('active', b.getAttribute('data-tab') === tabName);
    });

    Object.keys(elements.studioPanels).forEach(key => {
      if (elements.studioPanels[key]) {
        elements.studioPanels[key].classList.toggle('active', key === tabName);
      }
    });
  }
  window.switchStudioTab = switchStudioTab;

  // View: Reader
  function renderSidebarFiles(filterText = '') {
    if (!elements.readerSidebar) return;
    elements.readerSidebar.innerHTML = '';

    const filter = filterText.toLowerCase();

    window.KB_DATA.modules.forEach(m => {
      const matchedFiles = m.files.filter(f => 
        !filter || f.title.toLowerCase().includes(filter) || f.filename.toLowerCase().includes(filter)
      );

      if (matchedFiles.length === 0) return;

      const group = document.createElement('div');
      group.className = 'sidebar-module-group';
      group.innerHTML = `<div class="sidebar-group-title">Phân hệ ${m.badge}: ${m.title}</div>`;

      matchedFiles.forEach(f => {
        const item = document.createElement('div');
        item.className = 'sidebar-file-item';
        if (state.activeFile && state.activeFile.filename === f.filename) {
          item.classList.add('active');
        }
        item.innerHTML = `
          <span>${f.title}</span>
          <i class="fa-solid fa-angle-right" style="font-size: 0.75rem; opacity: 0.5;"></i>
        `;
        item.addEventListener('click', () => {
          renderFileContent(f);
        });
        group.appendChild(item);
      });

      elements.readerSidebar.appendChild(group);
    });

    if (elements.sidebarSearch) {
      elements.sidebarSearch.addEventListener('input', (e) => {
        renderSidebarFiles(e.target.value);
      });
    }
  }

  function renderFileContent(fileObj) {
    state.activeFile = fileObj;
    renderSidebarFiles(elements.sidebarSearch ? elements.sidebarSearch.value : '');

    if (elements.readerTitle) {
      elements.readerTitle.innerText = fileObj.title;
    }

    if (elements.readerContent) {
      if (window.marked) {
        elements.readerContent.innerHTML = window.marked.parse(fileObj.content);
      } else {
        elements.readerContent.innerHTML = `<pre>${fileObj.content}</pre>`;
      }
      elements.readerContent.style.fontSize = `${state.readerFontSize}px`;
    }
  }

  // Zoom controls in reader
  const zoomInBtn = document.getElementById('zoomInBtn');
  const zoomOutBtn = document.getElementById('zoomOutBtn');
  if (zoomInBtn) {
    zoomInBtn.addEventListener('click', () => {
      state.readerFontSize = Math.min(state.readerFontSize + 2, 24);
      if (elements.readerContent) elements.readerContent.style.fontSize = `${state.readerFontSize}px`;
    });
  }
  if (zoomOutBtn) {
    zoomOutBtn.addEventListener('click', () => {
      state.readerFontSize = Math.max(state.readerFontSize - 2, 12);
      if (elements.readerContent) elements.readerContent.style.fontSize = `${state.readerFontSize}px`;
    });
  }

  // View: Grammar Hub
  function renderGrammarHub() {
    const grid = document.getElementById('grammarGrid');
    if (!grid) return;
    grid.innerHTML = '';

    window.KB_DATA.grammarTopics.forEach(t => {
      const card = document.createElement('div');
      card.className = 'wp-card';
      card.innerHTML = `
        <div style="font-size: 0.8rem; font-weight: 700; color: var(--wp-blue); text-transform: uppercase;">
          Chủ điểm ${t.num}
        </div>
        <h3 class="wp-card-title" style="margin-top: 6px;">${t.title}</h3>
        <p class="wp-card-desc">Lý thuyết, bẫy thi, lỗi người Việt và bài tập so sánh B1 ➔ B2 đầy đủ 10 tiêu chí sư phạm.</p>
        <div class="wp-card-link">
          Đọc chuyên sâu <i class="fa-solid fa-arrow-right"></i>
        </div>
      `;
      card.addEventListener('click', () => {
        const topicNum = parseInt(t.num, 10);
        let targetFile = 'topics_01_10.md';
        if (topicNum > 10 && topicNum <= 20) targetFile = 'topics_11_20.md';
        else if (topicNum > 20) targetFile = 'topics_21_30.md';
        
        const grammarMod = window.KB_DATA.modules.find(m => m.id === '02_grammar');
        if (grammarMod) {
          const file = grammarMod.files.find(f => f.filename === targetFile);
          if (file) {
            renderFileContent(file);
            switchStudioTab('reader');
            const studioEl = document.getElementById('learning-studio');
            if (studioEl) studioEl.scrollIntoView({ behavior: 'smooth' });
          }
        }
      });
      grid.appendChild(card);
    });
  }

  // View: Vocabulary Hub
  function renderVocabHub() {
    const listContainer = document.getElementById('vocabTopicsList');
    if (!listContainer) return;
    listContainer.innerHTML = '';

    window.KB_DATA.vocabTopics.forEach(vt => {
      const card = document.createElement('div');
      card.className = 'wp-card';
      card.style.marginBottom = '20px';
      
      const wordsTags = vt.words.map(w => `<span class="kbd-badge" style="margin: 3px 4px; display: inline-block; cursor: pointer; background: var(--wp-light-blue); color: var(--wp-navy); padding: 4px 10px;" onclick="window.speakText('${w}')"><i class="fa-solid fa-volume-high" style="font-size:0.75rem; color: var(--wp-blue);"></i> ${w}</span>`).join(' ');

      card.innerHTML = `
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
          <span style="font-size: 0.8rem; font-weight: 700; color: var(--wp-blue); text-transform: uppercase;">Chủ đề ${vt.num}</span>
          <span style="font-size: 0.8rem; color: var(--wp-text-muted);">${vt.wordsCount} từ vựng B2</span>
        </div>
        <h3 class="wp-card-title">${vt.title}</h3>
        <div style="margin: 14px 0;">
          <strong style="font-size: 0.9rem; color: var(--wp-navy);">Từ vựng cốt lõi (Bấm để nghe phát âm):</strong>
          <div style="margin-top: 8px;">${wordsTags}</div>
        </div>
        <div style="background-color: var(--wp-light-blue); padding: 16px; border-radius: var(--radius-sm); margin-top: 12px; font-size: 0.92rem; border-left: 3px solid var(--wp-blue);">
          <p style="margin-bottom: 6px;"><strong style="color: var(--wp-navy);">Ví dụ câu B2:</strong> "${vt.example}"</p>
          ${vt.speaking ? `<p style="margin-bottom: 6px;"><strong style="color: var(--wp-navy);">Vận dụng Speaking:</strong> ${vt.speaking}</p>` : ''}
          ${vt.writing ? `<p><strong style="color: var(--wp-navy);">Vận dụng Writing:</strong> ${vt.writing}</p>` : ''}
        </div>
      `;
      listContainer.appendChild(card);
    });
  }

  // View: Flashcards (SRS System)
  function initFlashcards() {
    updateFlashcardsDeck(state.fcDeckFilter);

    if (elements.fcCard) {
      elements.fcCard.addEventListener('click', toggleFlashcardFlip);
    }

    if (elements.fcBtnAgain) {
      elements.fcBtnAgain.addEventListener('click', (e) => {
        e.stopPropagation();
        handleFlashcardRate(false);
      });
    }

    if (elements.fcBtnGood) {
      elements.fcBtnGood.addEventListener('click', (e) => {
        e.stopPropagation();
        handleFlashcardRate(true);
      });
    }

    if (elements.fcAudioBtn) {
      elements.fcAudioBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        const currentCard = state.fcList[state.fcIndex];
        if (currentCard) {
          window.speakText(currentCard.front);
        }
      });
    }

    if (elements.heroFcAudio) {
      elements.heroFcAudio.addEventListener('click', () => {
        const text = elements.heroFcWord ? elements.heroFcWord.innerText : 'curriculum';
        window.speakText(text);
      });
    }

    elements.deckButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        elements.deckButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const filter = btn.getAttribute('data-deck');
        updateFlashcardsDeck(filter);
      });
    });
  }

  function updateFlashcardsDeck(filter) {
    state.fcDeckFilter = filter;
    let list = window.KB_DATA.flashcards;

    if (filter === 'vocab') {
      list = list.filter(c => c.category === 'Vocabulary B2');
    } else if (filter === 'para') {
      list = list.filter(c => c.category === 'Paraphrase B1 ➔ B2');
    } else if (filter === 'mistakes') {
      list = list.filter(c => c.category === 'Trị Lỗi Sai L1');
    } else if (filter === 'wordfamily') {
      list = list.filter(c => c.category === 'Word Family Matrix');
    }

    state.fcList = list;
    state.fcIndex = 0;
    state.fcFlipped = false;
    renderCurrentFlashcard();
  }

  function renderCurrentFlashcard() {
    if (!elements.fcCard || state.fcList.length === 0) return;

    const card = state.fcList[state.fcIndex];
    state.fcFlipped = false;
    elements.fcCard.querySelector('.flashcard-inner').classList.remove('flipped');

    if (elements.fcCategory) elements.fcCategory.innerText = card.category;
    if (elements.fcFront) elements.fcFront.innerText = card.front;
    if (elements.fcBack) elements.fcBack.innerText = card.back;
    
    if (elements.fcCounter) {
      elements.fcCounter.innerText = `${state.fcIndex + 1} / ${state.fcList.length}`;
    }
    if (elements.fcStreak) {
      elements.fcStreak.innerText = state.fcStreak;
    }
  }

  function toggleFlashcardFlip() {
    state.fcFlipped = !state.fcFlipped;
    elements.fcCard.querySelector('.flashcard-inner').classList.toggle('flipped', state.fcFlipped);
  }

  function handleFlashcardRate(isSuccess) {
    const currentCard = state.fcList[state.fcIndex];
    if (isSuccess) {
      state.fcStreak += 1;
      localStorage.setItem('vstep_fc_streak', state.fcStreak.toString());
      if (currentCard && !state.fcMastered.includes(currentCard.id)) {
        state.fcMastered.push(currentCard.id);
        localStorage.setItem('vstep_fc_mastered', JSON.stringify(state.fcMastered));
      }
    } else {
      state.fcStreak = 0;
      localStorage.setItem('vstep_fc_streak', '0');
    }

    state.fcIndex = (state.fcIndex + 1) % state.fcList.length;
    renderCurrentFlashcard();
  }

  // View: Interactive Quiz
  function initQuiz() {
    state.quizIndex = 0;
    state.quizScore = 0;
    state.quizAnswered = false;
    renderCurrentQuiz();

    if (elements.quizNextBtn) {
      elements.quizNextBtn.addEventListener('click', () => {
        if (!state.quizAnswered) {
          showToast('Vui lòng chọn một phương án trước khi tiếp tục!');
          return;
        }

        if (state.quizIndex < window.KB_DATA.quizItems.length - 1) {
          state.quizIndex += 1;
          state.quizAnswered = false;
          renderCurrentQuiz();
        } else {
          showQuizSummary();
        }
      });
    }
  }

  function renderCurrentQuiz() {
    const q = window.KB_DATA.quizItems[state.quizIndex];
    if (!q) return;

    if (elements.quizCategory) elements.quizCategory.innerText = q.category;
    if (elements.quizQuestion) elements.quizQuestion.innerText = `${state.quizIndex + 1}. ${q.question}`;
    if (elements.quizProgress) {
      elements.quizProgress.innerText = `Câu ${state.quizIndex + 1} / ${window.KB_DATA.quizItems.length}`;
    }

    if (elements.quizExplanation) {
      elements.quizExplanation.classList.remove('show');
      elements.quizExplanation.innerHTML = '';
    }

    if (elements.quizOptions) {
      elements.quizOptions.innerHTML = '';
      q.options.forEach((opt, idx) => {
        const btn = document.createElement('button');
        btn.className = 'quiz-option-btn';
        btn.innerHTML = `<span style="width: 24px; font-weight:700; color: var(--wp-navy);">${String.fromCharCode(65 + idx)}.</span> <span>${opt}</span>`;
        btn.addEventListener('click', () => handleQuizSelect(idx, btn, q));
        elements.quizOptions.appendChild(btn);
      });
    }
  }

  function handleQuizSelect(selectedIdx, clickedBtn, q) {
    if (state.quizAnswered) return;
    state.quizAnswered = true;

    const allButtons = elements.quizOptions.querySelectorAll('.quiz-option-btn');
    allButtons.forEach(b => b.classList.add('disabled'));

    if (selectedIdx === q.answer) {
      clickedBtn.classList.add('correct');
      state.quizScore += 1;
      showToast('🎉 Chính xác! Bạn đã ghi điểm.', 'success');
      if (window.confetti) {
        window.confetti({ particleCount: 50, spread: 60, origin: { y: 0.8 } });
      }
    } else {
      clickedBtn.classList.add('wrong');
      allButtons[q.answer].classList.add('correct');
      showToast('❌ Chưa chính xác. Xem giải thích bên dưới.', 'error');
    }

    if (elements.quizExplanation) {
      elements.quizExplanation.innerHTML = `<strong style="color: var(--wp-navy);">💡 Giải thích chi tiết:</strong> ${q.explanation}`;
      elements.quizExplanation.classList.add('show');
    }
  }

  function showQuizSummary() {
    const total = window.KB_DATA.quizItems.length;
    const pct = Math.round((state.quizScore / total) * 100);

    if (elements.quizQuestion) {
      elements.quizQuestion.innerHTML = `
        <div style="text-align: center; padding: 24px 0;">
          <div style="font-size: 3.5rem; margin-bottom: 12px;">${pct >= 70 ? '🏆' : '📚'}</div>
          <h2 style="color: var(--wp-navy); margin-bottom: 8px;">Hoàn Thành Bài Kiểm Tra!</h2>
          <p style="font-size: 1.3rem; color: var(--wp-blue); font-weight: 700; margin: 12px 0;">
            Điểm số của bạn: ${state.quizScore} / ${total} (${pct}%)
          </p>
          <p style="color: var(--wp-text-secondary); max-width: 500px; margin: 0 auto 24px auto;">
            ${pct >= 80 ? 'Xuất sắc! Bạn nắm rất vững kiến thức và bẫy đề thi VSTEP B2.' : 'Rất tốt! Hãy tiếp tục ôn luyện các câu sai sót trong phần lý thuyết ngữ pháp.'}
          </p>
          <button class="btn btn-yellow" onclick="window.restartQuiz()">
            <i class="fa-solid fa-rotate-right"></i> Làm lại bài kiểm tra
          </button>
        </div>
      `;
    }

    if (elements.quizOptions) elements.quizOptions.innerHTML = '';
    if (elements.quizExplanation) elements.quizExplanation.classList.remove('show');
    if (elements.quizNextBtn) elements.quizNextBtn.style.display = 'none';

    if (pct >= 70 && window.confetti) {
      window.confetti({ particleCount: 120, spread: 100, origin: { y: 0.6 } });
    }
  }

  window.restartQuiz = function() {
    if (elements.quizNextBtn) elements.quizNextBtn.style.display = 'block';
    initQuiz();
  };

  // View: Checklist
  function initChecklist() {
    renderChecklist();
    updateReadinessMeter();
  }

  function renderChecklist() {
    if (!elements.checklistBody) return;
    elements.checklistBody.innerHTML = '';

    window.KB_DATA.checklistItems.forEach(item => {
      const currentStatus = state.checklist[item.id] || 'none';
      const tr = document.createElement('tr');
      tr.className = 'checklist-row';
      tr.innerHTML = `
        <td>${item.num}</td>
        <td>
          <div style="font-weight: 700; color: var(--wp-navy);">${item.title}</div>
          <div style="font-size: 0.84rem; color: var(--wp-text-secondary); margin-top: 4px;">${item.indicator}</div>
        </td>
        <td style="text-align: right; white-space: nowrap;">
          <button class="chk-status-btn red ${currentStatus === 'red' ? 'active' : ''}" title="Chưa đạt">🔴 Chưa đạt</button>
          <button class="chk-status-btn yellow ${currentStatus === 'yellow' ? 'active' : ''}" title="Đang hoàn thiện">🟡 Đang rèn</button>
          <button class="chk-status-btn green ${currentStatus === 'green' ? 'active' : ''}" title="Thành thạo">🟢 Thành thạo</button>
        </td>
      `;

      const btnRed = tr.querySelector('.chk-status-btn.red');
      const btnYellow = tr.querySelector('.chk-status-btn.yellow');
      const btnGreen = tr.querySelector('.chk-status-btn.green');

      btnRed.addEventListener('click', () => setChecklistStatus(item.id, 'red'));
      btnYellow.addEventListener('click', () => setChecklistStatus(item.id, 'yellow'));
      btnGreen.addEventListener('click', () => setChecklistStatus(item.id, 'green'));

      elements.checklistBody.appendChild(tr);
    });
  }

  function setChecklistStatus(itemId, status) {
    state.checklist[itemId] = status;
    localStorage.setItem('vstep_checklist', JSON.stringify(state.checklist));
    renderChecklist();
    updateReadinessMeter();
  }

  function updateReadinessMeter() {
    const total = window.KB_DATA.checklistItems.length;
    if (total === 0) return;

    let points = 0;
    Object.values(state.checklist).forEach(val => {
      if (val === 'green') points += 1;
      else if (val === 'yellow') points += 0.5;
    });

    const percent = Math.round((points / total) * 100);
    if (elements.readinessPercent) elements.readinessPercent.innerText = `${percent}%`;
    if (elements.readinessProgressBar) elements.readinessProgressBar.style.width = `${percent}%`;
    if (elements.heroReadiness) elements.heroReadiness.innerText = `${percent}%`;
  }

  // Global Search
  function setupGlobalSearch() {
    if (elements.searchTriggerBtn) {
      elements.searchTriggerBtn.addEventListener('click', openSearchModal);
    }
    if (elements.modalCloseBtn) {
      elements.modalCloseBtn.addEventListener('click', closeSearchModal);
    }
    if (elements.searchModal) {
      elements.searchModal.addEventListener('click', (e) => {
        if (e.target === elements.searchModal) closeSearchModal();
      });
    }
    if (elements.modalSearchInput) {
      elements.modalSearchInput.addEventListener('input', handleModalSearch);
    }
  }

  function openSearchModal() {
    if (!elements.searchModal) return;
    elements.searchModal.classList.add('open');
    if (elements.modalSearchInput) {
      elements.modalSearchInput.value = '';
      elements.modalSearchInput.focus();
    }
    if (elements.searchResultsList) {
      elements.searchResultsList.innerHTML = '<div style="padding: 24px; text-align: center; color: var(--wp-text-muted);">Gõ từ khóa để tra cứu toàn bộ 18 phân hệ, từ vựng, ngữ pháp...</div>';
    }
  }

  function closeSearchModal() {
    if (elements.searchModal) elements.searchModal.classList.remove('open');
  }

  function handleModalSearch(e) {
    const query = e.target.value.trim().toLowerCase();
    if (!query) {
      elements.searchResultsList.innerHTML = '<div style="padding: 24px; text-align: center; color: var(--wp-text-muted);">Gõ từ khóa để tìm kiếm...</div>';
      return;
    }

    const results = [];

    // Search Files
    window.KB_DATA.modules.forEach(m => {
      m.files.forEach(f => {
        if (f.title.toLowerCase().includes(query) || f.content.toLowerCase().includes(query)) {
          results.push({
            type: `Phân hệ ${m.badge}`,
            title: f.title,
            snippet: getSnippet(f.content, query),
            action: () => {
              renderFileContent(f);
              switchStudioTab('reader');
              closeSearchModal();
              const studioEl = document.getElementById('learning-studio');
              if (studioEl) studioEl.scrollIntoView({ behavior: 'smooth' });
            }
          });
        }
      });
    });

    // Search Vocab
    window.KB_DATA.vocabTopics.forEach(v => {
      const matchedWords = v.words.filter(w => w.toLowerCase().includes(query));
      if (matchedWords.length > 0 || v.title.toLowerCase().includes(query)) {
        results.push({
          type: 'Từ Vựng B2',
          title: `Chủ đề ${v.num}: ${v.title}`,
          snippet: `Khớp từ vựng: ${matchedWords.slice(0, 5).join(', ')}`,
          action: () => {
            switchStudioTab('vocab');
            closeSearchModal();
            const studioEl = document.getElementById('learning-studio');
            if (studioEl) studioEl.scrollIntoView({ behavior: 'smooth' });
          }
        });
      }
    });

    renderSearchResults(results);
  }

  function getSnippet(content, query) {
    const idx = content.toLowerCase().indexOf(query);
    if (idx === -1) return content.slice(0, 100) + '...';
    const start = Math.max(0, idx - 40);
    const end = Math.min(content.length, idx + 100);
    return '...' + content.slice(start, end).replace(/\n/g, ' ') + '...';
  }

  function renderSearchResults(results) {
    if (!elements.searchResultsList) return;

    if (results.length === 0) {
      elements.searchResultsList.innerHTML = '<div style="padding: 24px; text-align: center; color: var(--wp-text-muted);">Không tìm thấy kết quả phù hợp.</div>';
      return;
    }

    elements.searchResultsList.innerHTML = '';
    results.slice(0, 15).forEach(res => {
      const item = document.createElement('div');
      item.className = 'search-result-item';
      item.innerHTML = `
        <span class="result-badge">${res.type}</span>
        <div class="result-title">${res.title}</div>
        <div class="result-snippet">${res.snippet}</div>
      `;
      item.addEventListener('click', res.action);
      elements.searchResultsList.appendChild(item);
    });
  }

  function handleGlobalKeydown(e) {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      openSearchModal();
    }
    if (e.key === 'Escape') {
      closeSearchModal();
    }
    if (e.code === 'Space' && state.currentStudioTab === 'flashcards' && e.target.tagName !== 'INPUT') {
      e.preventDefault();
      toggleFlashcardFlip();
    }
  }

  window.speakText = function (text) {
    if (!('speechSynthesis' in window)) {
      showToast('Trình duyệt không hỗ trợ phát âm âm thanh.', 'error');
      return;
    }
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en-US';
    utterance.rate = 0.9;
    window.speechSynthesis.speak(utterance);
  };

  function showToast(message, type = 'info') {
    let container = document.getElementById('toastContainer');
    if (!container) {
      container = document.createElement('div');
      container.id = 'toastContainer';
      container.className = 'toast-container';
      document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.innerHTML = `
      <i class="fa-solid ${type === 'success' ? 'fa-circle-check' : (type === 'error' ? 'fa-circle-exclamation' : 'fa-circle-info')}" 
         style="color: var(--${type === 'success' ? 'wp-success' : (type === 'error' ? 'wp-danger' : 'wp-yellow')});"></i>
      <span>${message}</span>
    `;

    container.appendChild(toast);
    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px)';
      setTimeout(() => toast.remove(), 300);
    }, 3000);
  }

  document.addEventListener('DOMContentLoaded', init);

})();
