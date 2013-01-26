<%inherit file="../base.mak" />

<%def name="title()">
	Add Collection
</%def>

<%def name="body()">
Colelctions: </br>
	% for collection in $colections:
	Voucher = ${collection.voucher}
	% endfor
</%def>
