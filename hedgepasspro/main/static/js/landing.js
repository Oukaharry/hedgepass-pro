// 1. Initialize TradingView Charts
function initTradingViewCharts() {
    // Prop Chart (Simulating Active Buy)
    new TradingView.widget({
        container_id: "propChart",
        width: "100%",
        height: "100%",
        symbol: "OANDA:EURUSD",
        interval: "1",
        timezone: "Etc/UTC",
        theme: "dark",
        style: "1",
        locale: "en",
        toolbar_bg: "#f1f3f6",
        hide_side_toolbar: true,
        allow_symbol_change: false,
        save_image: false,
        studies: ["Volume@tv-basicstudies"], // Add volume for better visualization
        overrides: {
            "mainSeriesProperties.showCountdown": true,
            "paneProperties.background": "#1a1a1a",
            "paneProperties.vertGridProperties.color": "#2a2a2a",
            "paneProperties.horzGridProperties.color": "#2a2a2a",
            "symbolWatermarkProperties.color": "rgba(0, 0, 0, 0)",
            "scalesProperties.textColor": "#AAA",
        },
        drawings_access: {
            type: "black",
            tools: [{ name: "Buy", position: "top" }],
        },
    });

    // Live Chart (Simulating Active Sell)
    new TradingView.widget({
        container_id: "liveChart",
        width: "100%",
        height: "100%",
        symbol: "OANDA:GBPUSD",
        interval: "1",
        timezone: "Etc/UTC",
        theme: "dark",
        style: "1",
        locale: "en",
        toolbar_bg: "#f1f3f6",
        hide_side_toolbar: true,
        allow_symbol_change: false,
        save_image: false,
        studies: ["Volume@tv-basicstudies"], // Add volume for better visualization
        overrides: {
            "mainSeriesProperties.showCountdown": true,
            "paneProperties.background": "#1a1a1a",
            "paneProperties.vertGridProperties.color": "#2a2a2a",
            "paneProperties.horzGridProperties.color": "#2a2a2a",
            "symbolWatermarkProperties.color": "rgba(0, 0, 0, 0)",
            "scalesProperties.textColor": "#AAA",
        },
        drawings_access: {
            type: "black",
            tools: [{ name: "Sell", position: "top" }],
        },
    });
}

// 2. Simulate Metrics Computation
function initMetricsComputation() {
    const canvas = document.getElementById('metricsComputation');
    const ctx = canvas.getContext('2d');

    function resizeCanvas() {
        canvas.width = canvas.parentElement.clientWidth;
        canvas.height = canvas.parentElement.clientHeight;
    }

    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    let profit = 0;
    let loss = 0;

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Simulate metrics
        profit += Math.random() * 10 - 5;
        loss += Math.random() * 5 - 2;

        // Draw profit
        ctx.fillStyle = '#4CAF50';
        ctx.font = '20px Arial';
        ctx.fillText(`Profit: $${profit.toFixed(2)}`, 10, 30);

        // Draw loss
        ctx.fillStyle = '#FF5252';
        ctx.fillText(`Loss: $${loss.toFixed(2)}`, 10, 60);

        // Draw balance
        const balance = profit - loss;
        ctx.fillStyle = '#FFFFFF';
        ctx.fillText(`Balance: $${balance.toFixed(2)}`, 10, 90);

        requestAnimationFrame(animate);
    }

    animate();
}

// Initialize all animations
document.addEventListener('DOMContentLoaded', () => {
    initTradingViewCharts();
    initMetricsComputation();
});