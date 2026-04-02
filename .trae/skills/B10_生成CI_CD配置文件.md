---
name: B10 锟斤拷锟斤拷CI CD锟斤拷锟斤拷锟侥硷拷
description: 执锟斤拷 B10 锟斤拷锟斤拷CI CD锟斤拷锟斤拷锟侥硷拷 锟斤拷锟借，锟斤拷锟斤拷锟侥匡拷锟斤拷锟斤拷械锟斤拷囟锟斤拷锟斤拷锟?allowed-tools: Bash, Read, Write, SSH, Network
---
# B10_鐢熸垚CI_CD閰嶇疆鏂囦欢.md

## 鍓嶇疆鏉′欢
- `.ai/杩涘害鐘讹拷?json` 涓殑 `current_step` 蹇呴』锟?`B10`锟?- `B9.1` 宸插畬鎴愶拷?
## 鐩爣
鏍规嵁椤圭洰鎶€鏈爤鍜岄儴缃茬洰鏍囷紝鐢熸垚 CI/CD 閰嶇疆鏂囦欢锛堝 GitHub Actions銆丟itLab CI銆丣enkinsfile 绛夛級锟?
## Action
- 璇诲彇 `AGENTS.md` 涓殑鎶€鏈爤鍜岄儴缃查厤缃紙`.ai/config/deployment.yaml`锛夛拷?- 纭畾 CI/CD 骞冲彴锛堥粯锟?GitHub Actions锛屽彲璇㈤棶鐢ㄦ埛锛夛拷?- 鐢熸垚閰嶇疆鏂囦欢锟?  - 瑙﹀彂鏉′欢锛堝 push 锟?main/master锛宲ull request锟?  - 鏋勫缓姝ラ锛堝畨瑁呬緷璧栥€佽繍锟?lint銆佽繍琛屾祴璇曪級
  - 鏋勫缓浜х墿锛堝 Docker 闀滃儚銆佹墦鍖呮枃浠讹級
  - 閮ㄧ讲姝ラ锛堜笂浼犲埌鏈嶅姟鍣ㄣ€侀噸鍚湇鍔＄瓑锟?- 灏嗛厤缃枃浠跺啓鍏ラ」鐩牴鐩綍涓嬬殑瀵瑰簲璺緞锛堝 `.github/workflows/deploy.yml`锛夛拷?
## Assert
- 閰嶇疆鏂囦欢璇硶姝ｇ‘锛圷AML/JSON锛夛拷?- 鍖呭惈蹇呰鐨勭幆澧冨彉閲忓崰浣嶇锛堝 `${{ secrets.DEPLOY_KEY }}`锛夛拷?
## Artefact
- CI/CD 閰嶇疆鏂囦欢锛堝 `.github/workflows/deploy.yml`锛夛拷?
## Analysis
- 妫€鏌ユ槸鍚﹀凡鏈夌幇鎴愮殑 CI/CD 閰嶇疆锛岄伩鍏嶉噸澶嶆垨鍐茬獊锟?- 鑻ラ儴缃茬洰鏍囦负鑷缓鏈嶅姟鍣紝鐢熸垚鑴氭湰绀轰緥渚涚敤鎴峰弬鑰冿拷?
## Adjust
- 濡傛灉鐢ㄦ埛娌℃湁鎸囧畾 CI/CD 骞冲彴锛屼娇鐢ㄩ粯锟?GitHub Actions锟?- 鑻ラ厤缃腑娑夊強鏁忔劅淇℃伅锛屼娇鐢ㄧ幆澧冨彉閲忓崰浣嶇锛屾彁绀虹敤鎴疯锟?secrets锟?
## Advance
- 鏇存柊 `.ai/杩涘害鐘讹拷?json`锟?  ```json
  {
    "current_step": "B11",
    "steps_completed": ["...", "B10"]
  }
  ```
- 鎻愮ず鐢ㄦ埛锛氫笅涓€姝ュ簲鎵ц B11锟?
## 骞查
鏃狅紙鑷姩鐢熸垚锛岀敤鎴峰彲鍚庣画淇敼锛夛拷?
