/* ==========================================================================
   MOBILE PORTFOLIO INTERACTIVE CONTROLLER
   FastAPI + PWA + FAB Popup Menu + Bottom Nav Switcher
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
    initBottomNav();
    initFabMenu();
    initThemeToggle();
    initContactForm();
    initPwaInstall();
    initProgressBars();
    initAcadAccordion();
    initAcadQuickjump();
});

/**
 * Bottom Navigation Bar Tab Switcher
 */
function initBottomNav() {
    const navItems = document.querySelectorAll('.bottom-nav .nav-item');
    const tabContents = document.querySelectorAll('.tab-content');

    navItems.forEach(item => {
        item.addEventListener('click', () => {
            const targetTab = item.getAttribute('data-tab');

            // Deactivate all
            navItems.forEach(n => n.classList.remove('active'));
            tabContents.forEach(c => c.classList.remove('active'));

            // Activate clicked
            item.classList.add('active');
            const activeContent = document.getElementById(targetTab);
            if (activeContent) {
                activeContent.classList.add('active');
                if (targetTab === 'tab-academics') {
                    initProgressBars();
                }
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
        });
    });

    // Check URL parameters or hash on initial load (e.g. returning from certificate page)
    const urlParams = new URLSearchParams(window.location.search);
    const tabParam = urlParams.get('tab');
    const hash = window.location.hash.replace('#', '');
    
    let initialTab = tabParam || (hash.startsWith('tab-') ? hash : (hash === 'academics' ? 'tab-academics' : null));
    if (initialTab) {
        const targetBtn = document.querySelector(`.bottom-nav .nav-item[data-tab="${initialTab}"]`);
        if (targetBtn) {
            targetBtn.click();
        }
    }

    // Keyboard accessibility for achievement boxes
    document.querySelectorAll('.achievement-box, .achievement-activity-box').forEach(box => {
        box.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                box.click();
            }
        });
    });
}

/**
 * Floating Action Button (FAB) Radial Menu Controller
 */
function initFabMenu() {
    const fabBtn = document.getElementById('fabMainBtn');
    const fabMenu = document.getElementById('fabMenu');

    if (!fabBtn || !fabMenu) return;

    fabBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        const isOpen = fabBtn.classList.toggle('open');
        fabMenu.classList.toggle('open', isOpen);
    });

    // Close FAB menu when clicking anywhere else
    document.addEventListener('click', (e) => {
        if (!fabBtn.contains(e.target) && !fabMenu.contains(e.target)) {
            fabBtn.classList.remove('open');
            fabMenu.classList.remove('open');
        }
    });

    // FAB Action Items
    const themeBtn = document.getElementById('fabThemeToggle');
    if (themeBtn) {
        themeBtn.addEventListener('click', (e) => {
            e.preventDefault();
            toggleTheme();
            fabBtn.classList.remove('open');
            fabMenu.classList.remove('open');
        });
    }
}

/**
 * Dark / Light Glassmorphism Theme Switcher
 */
function initThemeToggle() {
    const savedTheme = localStorage.getItem('portfolio-theme') || 'dark';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('portfolio-theme', newTheme);
    updateThemeIcon(newTheme);
    showToast(`Switched to ${newTheme === 'dark' ? 'Dark Mode 🌙' : 'Light Mode ☀️'}`);
}

function updateThemeIcon(theme) {
    const icon = document.querySelector('#fabThemeToggle i');
    const text = document.querySelector('#fabThemeToggle span');
    if (icon && text) {
        if (theme === 'dark') {
            icon.className = 'fa-solid fa-sun';
            text.textContent = 'Light Mode';
        } else {
            icon.className = 'fa-solid fa-moon';
            text.textContent = 'Dark Mode';
        }
    }
}

/**
 * Interactive Contact Form Handling via FastAPI API
 */
function initContactForm() {
    const contactForm = document.getElementById('contactForm');
    const responseBox = document.getElementById('contactResponse');

    const directMailLink = document.getElementById('directMailtoLink');
    const updateMailto = () => {
        if (!directMailLink) return;
        const subj = encodeURIComponent(document.getElementById('msgSubject')?.value || 'Portfolio Contact Inquiry');
        const name = document.getElementById('senderName')?.value || '';
        const bodyText = document.getElementById('msgText')?.value || '';
        const body = encodeURIComponent(`From: ${name}\n\n${bodyText}`);
        directMailLink.href = `mailto:ynadewmini@gmail.com?subject=${subj}&body=${body}`;
    };

    ['senderName', 'msgSubject', 'msgText'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.addEventListener('input', updateMailto);
    });

    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const submitBtn = contactForm.querySelector('button[type="submit"]');
        const originalText = submitBtn.innerHTML;
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Sending to ynadewmini@gmail.com...';

        const formData = {
            name: document.getElementById('senderName').value,
            email: document.getElementById('senderEmail').value,
            subject: document.getElementById('msgSubject').value,
            message: document.getElementById('msgText').value
        };

        try {
            const res = await fetch('/api/contact', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            });

            const result = await res.json();
            if (res.ok) {
                showToast('Delivered to ynadewmini@gmail.com!');
                contactForm.reset();
                updateMailto();
                if (responseBox) {
                    responseBox.style.display = 'block';
                    responseBox.innerHTML = `<i class="fa-solid fa-circle-check"></i> ${result.message}`;
                    responseBox.className = 'glass-card contact-success';
                }
            } else {
                showToast('Submission error. Check inputs.');
                if (responseBox) {
                    responseBox.style.display = 'block';
                    responseBox.innerHTML = `<i class="fa-solid fa-circle-exclamation"></i> Submission error. Please verify your input.`;
                    responseBox.className = 'glass-card contact-error';
                }
            }
        } catch (err) {
            console.error('Contact error:', err);
            showToast('Network error while sending message.');
            if (responseBox) {
                responseBox.style.display = 'block';
                responseBox.innerHTML = `<i class="fa-solid fa-triangle-exclamation"></i> Network error while sending message. Please try again or use the mail app button.`;
                responseBox.className = 'glass-card contact-error';
            }
        } finally {
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalText;
        }
    });
}

/**
 * PWA Installation Controller
 */
let deferredPrompt;
function initPwaInstall() {
    const installBtn = document.getElementById('fabInstallPwa');
    
    window.addEventListener('beforeinstallprompt', (e) => {
        e.preventDefault();
        deferredPrompt = e;
        if (installBtn) installBtn.style.display = 'flex';
    });

    if (installBtn) {
        installBtn.addEventListener('click', async () => {
            if (!deferredPrompt) {
                showToast('App is already installed or supported natively!');
                return;
            }
            deferredPrompt.prompt();
            const { outcome } = await deferredPrompt.userChoice;
            if (outcome === 'accepted') {
                showToast('Portfolio App installed to Home Screen!');
            }
            deferredPrompt = null;
        });
    }
}

/**
 * Toast Notification Utility
 */
function showToast(message) {
    let toast = document.getElementById('toastNotification');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'toastNotification';
        toast.className = 'toast-notification';
        document.body.appendChild(toast);
    }

    toast.textContent = message;
    toast.classList.add('show');

    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

/**
 * Academic Progress Bar Animator
 * Fills progress bars smoothly from data-progress values
 */
function initProgressBars() {
    const bars = document.querySelectorAll('.progress-bar-fill[data-progress]');
    bars.forEach(bar => {
        const targetVal = bar.getAttribute('data-progress');
        if (targetVal) {
            // Reset to 0 then animate to target
            bar.style.width = '0%';
            requestAnimationFrame(() => {
                setTimeout(() => {
                    bar.style.width = `${targetVal}%`;
                }, 50);
            });
        }
    });
}


/**
 * Academic Page — Accordion Section Toggles
 */
function initAcadAccordion() {
    const toggles = document.querySelectorAll('.acad-section-toggle');
    toggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const expanded = toggle.getAttribute('aria-expanded') === 'true';
            const body = toggle.nextElementSibling;
            if (expanded) {
                toggle.setAttribute('aria-expanded', 'false');
                body.classList.remove('open');
            } else {
                toggle.setAttribute('aria-expanded', 'true');
                body.classList.add('open');
            }
        });
    });
}

/**
 * Academic Page — Quick-Jump Pill Navigation
 */
function initAcadQuickjump() {
    const pills = document.querySelectorAll('.acad-jump-pill');
    pills.forEach(pill => {
        pill.addEventListener('click', () => {
            pills.forEach(p => p.classList.remove('active'));
            pill.classList.add('active');
            const targetId = pill.getAttribute('data-target');
            const targetSection = document.getElementById(targetId);
            if (targetSection) {
                const toggle = targetSection.querySelector('.acad-section-toggle');
                const body = targetSection.querySelector('.acad-section-body');
                if (toggle && body && !body.classList.contains('open')) {
                    toggle.setAttribute('aria-expanded', 'true');
                    body.classList.add('open');
                }
                setTimeout(() => {
                    targetSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }, 80);
            }
        });
    });
}
