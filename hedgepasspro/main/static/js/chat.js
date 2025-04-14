// FAQ Toggle Functionality
document.querySelectorAll('.faq-question').forEach(button => {
    button.addEventListener('click', () => {
        const faqItem = button.parentElement;
        faqItem.classList.toggle('active');
        
        // Close other open FAQs
        document.querySelectorAll('.faq-item').forEach(item => {
            if (item !== faqItem && item.classList.contains('active')) {
                item.classList.remove('active');
            }
        });
    });
});

// Chat Widget Toggle
const chatToggle = document.getElementById('chat-toggle');
const chatWidget = document.getElementById('chat-widget');
const closeChat = document.getElementById('close-chat');

chatToggle.addEventListener('click', () => {
    chatWidget.classList.toggle('active');
});

closeChat.addEventListener('click', () => {
    chatWidget.classList.remove('active');
});

// Quick Question Buttons
document.querySelectorAll('.quick-question').forEach(button => {
    button.addEventListener('click', () => {
        const question = button.textContent;
        const chatMessages = document.querySelector('.chat-messages');
        
        // Add user question
        const userMessage = document.createElement('div');
        userMessage.classList.add('chat-user-message');
        userMessage.innerHTML = `<p>${question}</p>`;
        chatMessages.appendChild(userMessage);
        
        // Simulate bot response
        setTimeout(() => {
            const botResponse = document.createElement('div');
            botResponse.classList.add('chat-bot-message');
            
            let responseText = "Here's some information about that topic...";
            // Custom responses for different questions
            if (question.includes("VPS")) {
                responseText = "Our platform doesn't require a VPS. All operations are handled through our secure cloud infrastructure, complying with prop firm regulations.";
            } else if (question.includes("Setup")) {
                responseText = "Account setup takes just 3 steps: 1) Create your account 2) Connect your MT5 details 3) Configure your preferences. Our wizard will guide you through each step.";
            }
            
            botResponse.innerHTML = `<p>${responseText}</p>`;
            chatMessages.appendChild(botResponse);
            
            // Scroll to bottom
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }, 800);
    });
});

// Live Agent Request
document.getElementById('request-agent').addEventListener('click', () => {
    const chatMessages = document.querySelector('.chat-messages');
    
    const botResponse = document.createElement('div');
    botResponse.classList.add('chat-bot-message');
    botResponse.innerHTML = `<p>We're connecting you to a live agent. Please hold while we transfer your chat. In the meantime, you can continue typing your question below.</p>`;
    chatMessages.appendChild(botResponse);
    
    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
});

// Add to chat.js
window.addEventListener('resize', function() {
    if (window.balanceChart) {
        window.balanceChart.resize();
    }
});