# Github-Chess

[Click](https://fictional-orbit-67v7r47r9q9f57wx-5000.app.github.dev/move?game=abc123&move=e2e4&redirect=https://github.com/AragornOfKebroyd/Github-Chess)


```<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>8x8 Radio Grid</title>
    <style>
        /* CSS for chessboard-like grid */
        .grid-container {
            display: grid;
            grid-template-columns: repeat(8, 60px); /* 8 equal columns, 60px each */
            grid-template-rows: repeat(8, 60px); /* 8 equal rows, 60px each */
            gap: 0; /* No gaps for seamless chessboard look */
            border: 2px solid #333;
            width: fit-content;
        }
        
        .grid-item {
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        /* Hide the actual radio button */
        .grid-item input[type="radio"] {
            display: none;
        }
        
        /* Style the label as a clickable square */
        .grid-item label {
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s ease;
            font-size: 0; /* Hide all text */
        }
        
        /* Chessboard alternating pattern */
        .grid-item label {
            background-color: #f0d9b5; /* Light squares by default */
        }
        
        /* Create proper chessboard pattern */
        .grid-item:nth-child(16n+1) label,
        .grid-item:nth-child(16n+3) label,
        .grid-item:nth-child(16n+5) label,
        .grid-item:nth-child(16n+7) label,
        .grid-item:nth-child(16n+10) label,
        .grid-item:nth-child(16n+12) label,
        .grid-item:nth-child(16n+14) label,
        .grid-item:nth-child(16n+16) label {
            background-color: #b58863; /* Dark squares */
        }
        
        /* Hover effects */
        .grid-item label:hover {
            background-color: #87ceeb !important;
            transform: scale(0.95);
        }
        
        /* Selected state */
        .grid-item input[type="radio"]:checked + label {
            background-color: #4CAF50 !important;
            box-shadow: inset 0 0 10px rgba(0,0,0,0.3);
        }
    </style>
</head>
<body>

    <h1>8x8 Grid (Select One Square)</h1>
    
    <div class="grid-container">
        <div class="grid-item"><input type="radio" name="grid_selection" value="a8" id="a8"><label for="a8">A8</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="b8" id="b8"><label for="b8">B8</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="c8" id="c8"><label for="c8">C8</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="d8" id="d8"><label for="d8">D8</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="e8" id="e8"><label for="e8">E8</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="f8" id="f8"><label for="f8">F8</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="g8" id="g8"><label for="g8">G8</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="h8" id="h8"><label for="h8">H8</label></div>
        
        <div class="grid-item"><input type="radio" name="grid_selection" value="a7" id="a7"><label for="a7">A7</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="b7" id="b7"><label for="b7">B7</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="c7" id="c7"><label for="c7">C7</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="d7" id="d7"><label for="d7">D7</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="e7" id="e7"><label for="e7">E7</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="f7" id="f7"><label for="f7">F7</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="g7" id="g7"><label for="g7">G7</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="h7" id="h7"><label for="h7">H7</label></div>

        <div class="grid-item"><input type="radio" name="grid_selection" value="a6" id="a6"><label for="a6">A6</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="b6" id="b6"><label for="b6">B6</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="c6" id="c6"><label for="c6">C6</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="d6" id="d6"><label for="d6">D6</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="e6" id="e6"><label for="e6">E6</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="f6" id="f6"><label for="f6">F6</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="g6" id="g6"><label for="g6">G6</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="h6" id="h6"><label for="h6">H6</label></div>

        <div class="grid-item"><input type="radio" name="grid_selection" value="a5" id="a5"><label for="a5">A5</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="b5" id="b5"><label for="b5">B5</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="c5" id="c5"><label for="c5">C5</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="d5" id="d5"><label for="d5">D5</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="e5" id="e5"><label for="e5">E5</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="f5" id="f5"><label for="f5">F5</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="g5" id="g5"><label for="g5">G5</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="h5" id="h5"><label for="h5">H5</label></div>

        <div class="grid-item"><input type="radio" name="grid_selection" value="a4" id="a4"><label for="a4">A4</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="b4" id="b4"><label for="b4">B4</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="c4" id="c4"><label for="c4">C4</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="d4" id="d4"><label for="d4">D4</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="e4" id="e4"><label for="e4">E4</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="f4" id="f4"><label for="f4">F4</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="g4" id="g4"><label for="g4">G4</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="h4" id="h4"><label for="h4">H4</label></div>

        <div class="grid-item"><input type="radio" name="grid_selection" value="a3" id="a3"><label for="a3">A3</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="b3" id="b3"><label for="b3">B3</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="c3" id="c3"><label for="c3">C3</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="d3" id="d3"><label for="d3">D3</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="e3" id="e3"><label for="e3">E3</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="f3" id="f3"><label for="f3">F3</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="g3" id="g3"><label for="g3">G3</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="h3" id="h3"><label for="h3">H3</label></div>

        <div class="grid-item"><input type="radio" name="grid_selection" value="a2" id="a2"><label for="a2">A2</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="b2" id="b2"><label for="b2">B2</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="c2" id="c2"><label for="c2">C2</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="d2" id="d2"><label for="d2">D2</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="e2" id="e2"><label for="e2">E2</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="f2" id="f2"><label for="f2">F2</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="g2" id="g2"><label for="g2">G2</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="h2" id="h2"><label for="h2">H2</label></div>

        <div class="grid-item"><input type="radio" name="grid_selection" value="a1" id="a1"><label for="a1">A1</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="b1" id="b1"><label for="b1">B1</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="c1" id="c1"><label for="c1">C1</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="d1" id="d1"><label for="d1">D1</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="e1" id="e1"><label for="e1">E1</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="f1" id="f1"><label for="f1">F1</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="g1" id="g1"><label for="g1">G1</label></div>
        <div class="grid-item"><input type="radio" name="grid_selection" value="h1" id="h1"><label for="h1">H1</label></div>
        
        </div>


</body>
</html>```
