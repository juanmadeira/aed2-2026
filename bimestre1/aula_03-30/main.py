from tad_cafe import Cafeteira

c = Cafeteira(1000)

c.ver_status()
c.ligar()
c.ver_status()
c.abastecer_agua(600)
c.ver_status()
c.abastecer_cafe(200)
c.ver_status()
c.fazer_cafe()