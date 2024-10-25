import justpy as jp

def app():
  wp = jp.QuasarPage()
  h1 = jp.QDiv(a=wp, text="Analysis Of Course Reviews", classes="text-h3 text-center q-pa-md")
  p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis", classes="text-body1")

  
  return wp;

jp.justpy(app)

