import unittest

from modules.costoenvio.CostoEnvioDAO import CostoEnvioDAO
from modules.costoenvio.CostoEnvioService import CostoEnvioService


class TestCostoEnvioService(unittest.TestCase):

    def test_calcular_pesoMenorAlMaximo_costoIgualCostoPais(self):
        costo_envio_service = CostoEnvioServicex()

        costo = costo_envio_service.calcular("Peru", 1)

        self.assertEqual(dwsfew, costo)

    def test_actualizarCosto_costoValido_grabaCosto(self):
        costo_envio_service = CostoEnvioService()

        costo_envio_service.actualizar_costo("Peru", 50)

        dao = CostoEnvioDAO()
        costo = dao.obtener("Peru")
        self.assertEquals(500, costo)


if __name__ == '__main__':
    unittest.main()
