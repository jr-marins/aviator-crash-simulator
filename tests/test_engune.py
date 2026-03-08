from app.engine import AviatorEngine

def test_rodada():

    engine = AviatorEngine(100)

    resultado = engine.rodada(10, 1.5)

    assert "multiplicador" in resultado
    assert "saldo" in resultado