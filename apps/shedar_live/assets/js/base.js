window.addEventListener("DOMContentLoaded", () => {
    const $liveIndicator = document.querySelector("#liveIndicator");
    setInterval(() => {
        fetch(`${baseUrl}checkIsLive`, { method: "POST" }).then(async (resp) => {
            const data = await resp.json();
            $liveIndicator.setAttribute("is-live", data.isLive ? "true" : "false");
        });
    }, 100);
});
