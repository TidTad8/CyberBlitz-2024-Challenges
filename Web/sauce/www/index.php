<?php
$x = $_GET['x'] ?? '';
$y = $_GET['y'] ?? '';

if(preg_match('/^[a-zA-Z0-9_]*$/', $x)) {
    show_source(__FILE__);
} else {
    $x('', $y);
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Only exes and whys</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        .welcome {
            text-align: center;
            padding: 20px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
        }
    </style>
</head>
<body>
    <div class="welcome">
        <h1>Nonsensical!</h1>
    </div>
</body>
</html>