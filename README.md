<h1 align="center">GitHub Chess</h1>
<p align="center">Play chess entirely through a GitHub README!</p>

---

<h2 align="center">Choose Your Side</h2>

<p align="center">
  <!-- These links should trigger your Flask endpoint or workflow to register the player -->
  <a href="https://github.com/AragornOfKebroyd/Github-Chess/tree/main/play/white">
    <img src="https://img.shields.io/badge/Play_as_White-ffffff?style=for-the-badge" width=200 />
  </a>
  &nbsp;&nbsp;
  <a href="https://github.com/AragornOfKebroyd/Github-Chess/tree/main/play/black">
    <img src="https://img.shields.io/badge/Play_as_Black-000000?style=for-the-badge" width=200 />
  </a>
</p>

---

<table align="center">
  <tr>
    <!-- Left: Chessboard -->
    <td>
      <img src="https://fictional-orbit-67v7r47r9q9f57wx-5000.app.github.dev/displayboard" width="512" height="512" />
    </td>
    <!-- Right: Status Panel -->
    <td style="vertical-align: top; padding-left: 20px;">
      <table>
        <tr>
          <th>Status</th>
          <th>Details</th>
        </tr>
        <tr>
          <td><b>Current Turn</b></td>
          <td>White</td>
        </tr>
        <tr>
          <td><b>Last Move</b></td>
          <td>e2 → e4</td>
        </tr>
        <tr>
          <td><b>Game ID</b></td>
          <td>abc123</td>
        </tr>
        <tr>
          <td><b>Refresh</b></td>
          <td valign="middle" align="center">
            <a href="https://github.com/AragornOfKebroyd/Github-Chess">
              <img src="https://img.shields.io/badge/Refresh-000088?style=for-the-badge?logo=refresh?logoColor=white" height=22/>
            </a>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>

---

### **How to Play**

1. Click on the board to select a piece  
2. Then click a valid destination square  
3. GitHub will trigger a move via workflow → commit updated board  
4. You may need to **refresh the page** to see the latest move  
5. No take-backs (unless you hack the commit history 😏)

---

### **How This Works**

✅ Each square on the board is an `<img>` with a link to `/move?from=A2&to=A4`  
✅ Moves trigger a `repository_dispatch` event  
✅ A GitHub Action updates `state.json` + `README.md` + board SVG  
✅ No live JavaScript. Just GitHub being abused beautifully.

---

### **Tech Used**

| Component      | Purpose                        |
|----------------|--------------------------------|
| `Flask`        | Serves board images + routes   |
| `python-chess` | Game logic + move validation   |
| `GitHub Actions` | Processes moves + commits updates |
| `SVG / PNG`    | Board rendering                |
| `README.md`    | The entire game UI             |

---

<p align="center">
  <sub>Built for the hackathon theme: <strong>“Unintended Behaviour”</strong> — turning GitHub into a real-time chess platform.</sub>
</p>

