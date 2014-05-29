<html>
<head>
<title>Clean Up Schoolwires HTML</title>
</head>
<body>
<form method="POST">
<p>Input HTML or URL<br />
<textarea rows="10" cols="120" name="source">{{ source }}</textarea></p>
<p>Cleaned HTML<br />
<textarea rows="20" cols="120" name="output">{{ cleaned }}</textarea></p>
<p>Rejected Tags<br />
{{ rejected }}</p>
<p><input type="submit" name="submit" value="Submit" /></p>
</form>
</body>
</html>
