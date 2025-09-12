export default function handler(req, res) {
  const ua = req.headers['user-agent'] || "";

  if (/android/i.test(ua)) {
    res.writeHead(302, { Location: "https://play.google.com/store/apps/details?id=com.cncspa.app" });
  } else if (/iPhone|iPad|iPod/i.test(ua)) {
    res.writeHead(302, { Location: "https://apps.apple.com/it/app/orospay/id1522538511?l=en-GB" });
  } else {
    res.writeHead(302, { Location: "/" });
  }
  res.end();
}
