/* 原型共享交互 */
const FlowStore = {
  get() {
    try { return JSON.parse(sessionStorage.getItem('ts_flow') || '{}'); } catch { return {}; }
  },
  set(data) {
    sessionStorage.setItem('ts_flow', JSON.stringify({ ...this.get(), ...data }));
  },
  clear() { sessionStorage.removeItem('ts_flow'); }
};

function showToast(message, type = 'info') {
  let wrap = document.querySelector('.toast-wrap');
  if (!wrap) {
    wrap = document.createElement('div');
    wrap.className = 'toast-wrap';
    document.body.appendChild(wrap);
  }
  const el = document.createElement('div');
  el.className = 'toast' + (type !== 'info' ? ' ' + type : '');
  el.textContent = message;
  wrap.appendChild(el);
  setTimeout(() => el.remove(), 3200);
}

function openModal(id) {
  document.getElementById(id)?.classList.add('open');
}
function closeModal(id) {
  document.getElementById(id)?.classList.remove('open');
}

function confirmDialog(title, message) {
  return new Promise((resolve) => {
    let overlay = document.getElementById('global-confirm');
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.id = 'global-confirm';
      overlay.className = 'confirm-overlay';
      overlay.innerHTML = `
        <div class="confirm-box">
          <h3 id="confirm-title"></h3>
          <p id="confirm-msg"></p>
          <div class="confirm-actions">
            <button class="btn btn-secondary" id="confirm-cancel">取消</button>
            <button class="btn btn-primary" id="confirm-ok">确定</button>
          </div>
        </div>`;
      document.body.appendChild(overlay);
    }
    document.getElementById('confirm-title').textContent = title;
    document.getElementById('confirm-msg').textContent = message;
    overlay.classList.add('open');
    const ok = () => { overlay.classList.remove('open'); cleanup(); resolve(true); };
    const cancel = () => { overlay.classList.remove('open'); cleanup(); resolve(false); };
    const cleanup = () => {
      document.getElementById('confirm-ok').removeEventListener('click', ok);
      document.getElementById('confirm-cancel').removeEventListener('click', cancel);
    };
    document.getElementById('confirm-ok').addEventListener('click', ok);
    document.getElementById('confirm-cancel').addEventListener('click', cancel);
  });
}

/** 提交后跳转：携带范式来源与工时统计 */
async function submitTimesheet(opts) {
  const {
    paradigm = 'A',
    totalHours = 44.5,
    autoHours = 38.5,
    pendingHours = 6,
    week = 'W21',
    unassigned = 0
  } = opts;

  if (unassigned > 0) {
    showToast('还有 ' + unassigned + 'h 未分配项目活动，请先处理', 'error');
    return false;
  }

  const ok = await confirmDialog(
    '确认提交本周工时？',
    '合计 ' + totalHours + 'h。其中 Booking 内 ' + autoHours + 'h 将自动接收，超 Booking ' + pendingHours + 'h 需项目经理审批。提交后可修改已驳回记录。'
  );
  if (!ok) return false;

  FlowStore.set({ paradigm, totalHours, autoHours, pendingHours, week, submittedAt: new Date().toISOString() });
  window.location.href = 'flow-submitted.html?from=' + encodeURIComponent(paradigm);
  return true;
}

document.addEventListener('click', (e) => {
  if (e.target.classList.contains('modal-overlay')) {
    e.target.classList.remove('open');
  }
});
