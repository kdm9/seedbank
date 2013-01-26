<%inherit file="../base.mak" />
<%def name="styleSheetIncludes()">
</%def>
<%def name="javascriptIncludes()">
</%def>

<%def name="title()">
	Add Collection
</%def>

<%def name="bodyheader()">
</%def>

<%def name="body()">
Collections: <br />
% for collection in collections:
Voucher: ${collection["voucher"]} <br />
% endfor
</%def>
