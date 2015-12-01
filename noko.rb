require 'nokogiri'

@doc = Nokogiri::HTML::DocumentFragment.parse <<-EOHTML
<body>
  <h1>Three's Company</h1>
  <div>A love triangle.</div>
</body>
EOHTML

h1 = @doc.at_css "h1"
h1.content = "<script src='malicious'>Snap, Crackle & Pop</script>"

puts @doc.to_html
