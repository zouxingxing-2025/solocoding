---
name: D9 锟斤拷锟斤拷SSL证锟斤拷
description: 执锟斤拷 D9 锟斤拷锟斤拷SSL证锟斤拷 锟斤拷锟借，锟斤拷锟斤拷锟侥匡拷锟斤拷锟斤拷械锟斤拷囟锟斤拷锟斤拷锟?allowed-tools: Bash, Read, Write, Network
---
# D9_閰嶇疆SSL璇佷功.md

## 鍓嶇疆鏉′欢
- `.ai/杩涘害鐘讹拷?json` 涓殑 `current_step` 蹇呴』锟?`D9`锟?- `D8` 宸插畬鎴愶紙鍙嶅悜浠ｇ悊宸查厤缃級锟?
## 鐩爣
涓哄煙鍚嶉厤锟?SSL 璇佷功锛屽惎锟?HTTPS 璁块棶銆備紭鍏堜娇锟?Let's Encrypt 鑷姩鐢宠鍜岀画鏈燂拷?
## Action
- 璇诲彇 `.ai/config/deployment.yaml` 涓殑鍩熷悕鍜岄偖绠憋拷?- 妫€鏌ユ槸鍚﹀凡瀹夎 `certbot`锛岃嫢鏈畨瑁呭垯鎻愮ず鐢ㄦ埛瀹夎锛堟彁渚涘懡浠わ級锟?- 杩愯 `certbot --nginx -d example.com -d www.example.com --non-interactive --agree-tos --email your@email.com`锛堟浛鎹负瀹為檯鍩熷悕鍜岄偖绠憋級锟?- 鑻ヨ嚜鍔ㄧ敵璇峰け璐ワ紙濡傚煙鍚嶆湭瑙ｆ瀽锛夛紝杈撳嚭閿欒骞舵彁绀虹敤鎴锋墜鍔ㄧ敵璇凤拷?- 閰嶇疆璇佷功鑷姩缁湡锛堟坊锟?cron 浠诲姟锟?systemd timer锛夛拷?- 娴嬭瘯 HTTPS 璁块棶锛坄curl -I https://example.com`锛夛拷?
## Assert
- 璇佷功鎴愬姛鑾峰彇骞跺畨瑁咃拷?- Nginx 閰嶇疆宸叉洿鏂颁负鐩戝惉 443 绔彛骞跺惎锟?SSL锟?- HTTPS 璁块棶杩斿洖 200 鐘舵€佺爜锟?
## Artefact
- 璇佷功鏂囦欢璺緞璁板綍锛坄.ai/config/ssl_info.txt`锛夛拷?- 閮ㄧ讲鏃ュ織锛坄.ai/logs/ssl_setup.log`锛夛拷?
## Analysis
- 鑻ュ煙鍚嶆湭澶囨鎴栬В鏋愭湭鐢熸晥锛屾彁绀虹敤鎴峰厛瀹屾垚 DNS 璁剧疆锟?- 妫€鏌ラ槻鐏鏄惁寮€锟?443 绔彛锟?
## Adjust
- 濡傛灉鑷姩鐢宠澶辫触锛屾彁渚涙墜鍔ㄧ敵璇锋楠わ紙濡備粠浜戞湇鍔″晢涓嬭浇璇佷功锛夛拷?- 鑻ョ敤鎴峰凡鏈夎瘉涔︼紝鍏佽涓婁紶骞舵墜鍔ㄩ厤缃拷?
## Advance
- 鏇存柊 `.ai/杩涘害鐘讹拷?json`锟?  ```json
  {
    "current_step": "D10",
    "steps_completed": ["...", "D9"]
  }
  ```
- 鎻愮ず鐢ㄦ埛锛氫笅涓€姝ュ簲鎵ц D10锟?
## 骞查
闇€瑕佺敤鎴风‘璁ゅ煙鍚嶈В鏋愬凡鐢熸晥锟?
鑻ヨ嚜鍔ㄧ敵璇峰け璐ワ紝闇€鐢ㄦ埛鎵嬪姩鎻愪緵璇佷功锟?
