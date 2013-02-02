<!DOCTYPE html>
<html>
	<head>
		<title>Seedbank${next.title()}</title>
		<meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
		<meta name="keywords" content="seedbank seed plant collection database" />
		<meta name="description" content="Seedbank" />
		<link rel="shortcut icon" href="${request.static_url('seedbank:static/favicon.ico')}" />
		<link rel="stylesheet" href="${request.static_url('seedbank:static/css/base.css')}" type="text/css" media="screen" charset="utf-8" />
		${next.styleSheetIncludes()}
		<script type="text/javascript" href="${request.static_url('seedbank:static/js/jquery.js')}" />
		${next.javascriptIncludes()}
	</head>
	<body>
		<div class="bodyheader">
			${next.bodyheader()}
		</div>
		<div class="body">
			${next.body()}
		</div>
		<div class="bodyfooter">
			${next.bodyfooter()}
		</div>
	</body>
</html>
