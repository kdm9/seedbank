<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" xmlns:tal="http://xml.zope.org/namespaces/tal">
	<head>
		<title>Seedbank - ${next.title()}</title>
		<meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
		<meta name="keywords" content="python web application" />
		<meta name="description" content="pyramid web application" />
		<link rel="shortcut icon" href="${request.static_url('seedbank:static/favicon.ico')}" />
		<link rel="Stylesheet" href="${h.url('/css/base.css')}" />
		${next.styleSheetIncludes()}

		<--! js -->
		${next.javascriptIncludes()}
	</head>
	<body>
		<div class="header">
			${next.bodyheader()}
		</div>
		<div class="body">
			${next.body()}
		</div>
	</body>
</html>
