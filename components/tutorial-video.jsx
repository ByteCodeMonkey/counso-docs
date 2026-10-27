// Mintlify provides React hooks to snippets without a React import.
export const TutorialVideo = ({ videoId, title, language = "en" }) => {
  const [attempt, setAttempt] = useState(0);
  const [status, setStatus] = useState("loading");
  const host = useRef(null);
  const chinese = language === "zh-cn";

  useEffect(() => {
    setStatus("loading");
    let player;
    let disposed = false;
    let ready = false;
    let failed = false;
    let poll;
    const fail = (reason = "error") => {
      failed = true;
      if (!disposed) setStatus(reason);
      clearInterval(poll);
      clearTimeout(timeout);
    };
    // A blocked API script may never emit a player error. Bound that wait too.
    const timeout = setTimeout(() => {
      if (!ready) {
        const script = document.getElementById("counso-youtube-api");
        if (script && !window.YT?.Player) script.dataset.failed = "true";
        fail();
      }
    }, 15000);

    if (!window.YT?.Player) {
      let previous = document.getElementById("counso-youtube-api");
      if (previous?.dataset.failed === "true") {
        previous.remove();
        previous = null;
      }
      if (!window.onYouTubeIframeAPIReady) {
        window.onYouTubeIframeAPIReady = () => {};
      }
      if (!previous) {
        const script = document.createElement("script");
        script.id = "counso-youtube-api";
        script.src = "https://www.youtube.com/iframe_api";
        script.async = true;
        script.onerror = () => { script.dataset.failed = "true"; fail(); };
        document.head.appendChild(script);
      }
    }

    const connect = () => {
      if (disposed || failed || !window.YT?.Player || player || !host.current) return;
      clearInterval(poll);
      // React owns the host, while YouTube owns its children and their cleanup.
      const iframe = document.createElement("iframe");
      iframe.title = title;
      iframe.src = `https://www.youtube-nocookie.com/embed/${videoId}?enablejsapi=1&autoplay=0&playsinline=1&origin=${encodeURIComponent(window.location.origin)}`;
      iframe.allow = "encrypted-media; picture-in-picture; fullscreen";
      iframe.allowFullscreen = true;
      iframe.referrerPolicy = "strict-origin-when-cross-origin";
      iframe.style.cssText = "width:100%;height:100%;border:0;display:block";
      host.current.replaceChildren(iframe);
      player = new window.YT.Player(iframe, {
        events: {
          onReady: () => {
            if (disposed || failed) return;
            ready = true;
            clearTimeout(timeout);
            if (!disposed) setStatus("ready");
          },
          onError: () => fail("unavailable"),
        },
      });
    };
    poll = setInterval(connect, 150);
    connect();
    return () => {
      disposed = true;
      clearTimeout(timeout);
      clearInterval(poll);
      if (player) player.destroy();
    };
  }, [attempt, videoId, title]);

  const start = () => {
    setStatus("loading");
    setAttempt((value) => value + 1);
  };
  const fallback = status === "error" || status === "unavailable";

  return (
    <div className="my-4">
      <div className="relative w-full aspect-video min-h-[200px] overflow-hidden rounded-xl border border-slate-200 bg-slate-50 dark:border-slate-700 dark:bg-slate-900">
        <div ref={host} className={`absolute inset-0 ${status === "ready" ? "visible" : "invisible"}`} />
        {fallback && (
          <div className="absolute inset-0 flex flex-col items-center justify-center gap-3 p-5 text-center">
            <span aria-hidden="true" className="text-3xl text-slate-500">!</span>
            <span className="font-semibold text-slate-900 dark:text-slate-100">{title}</span>
              <p role="status" className="m-0 text-sm text-slate-600 dark:text-slate-300">
                {status === "unavailable"
                  ? (chinese ? "暂时无法播放此视频，请稍后重试。" : "This video is currently unavailable. Please try again later.")
                  : (chinese ? "暂时无法连接 YouTube，请检查网络连接后重试。你也可以继续阅读下方文字教程。" : "Unable to connect to YouTube. Check your network connection and retry, or continue with the written guide below.")}
              </p>
            <button type="button" onClick={start} className="rounded-lg bg-blue-600 px-4 py-2 text-sm font-medium text-white focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-blue-600">
              {chinese ? "重试" : "Retry"}
            </button>
          </div>
        )}
        {status === "loading" && (
          <div role="status" className="absolute inset-0 flex flex-col items-center justify-center gap-3 p-5 text-center text-sm text-slate-600 dark:text-slate-300">
            <span aria-hidden="true" className="h-6 w-6 animate-spin rounded-full border-2 border-slate-300 border-t-blue-600 motion-reduce:animate-none" />
            <span>{chinese ? "正在连接 YouTube，加载视频…" : "Connecting to YouTube and loading video…"}</span>
          </div>
        )}
      </div>
    </div>
  );
};
