from __future__ import annotations

import os
from inspect import getframeinfo, stack
from typing import Optional

from colorama import Fore, Style


class SingletonMeta(type):
    _instance: Optional[SingletonMeta] = None

    def __call__(self) -> SingletonMeta:
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class Logger(metaclass=SingletonMeta):

    def erro(self, err):
        self.escrever(Fore.RED, err, "ERRO")

    def dado(self, dado):
        self.escrever(Fore.CYAN, dado, "DADO")

    def flag(self, dado):
        self.escrever(Fore.BLUE, dado, "FLAG")

    def variavel(self, var, valor):
        self.escrever(Fore.GREEN, str(valor), var)

    def escrever(self, cor, info, texto_aux):
        caller = getframeinfo(stack()[2][0])

        print(
            Style.BRIGHT
            + os.path.basename(caller.filename)
            + Style.NORMAL
            + ":{0}:{1}\t".format(caller.function, caller.lineno)
            + cor
            + Style.BRIGHT
            + texto_aux
            + Style.NORMAL
            + ": "
            + info
            + Style.RESET_ALL
        )

    def tempo(
        self,
        i_frame,
        tempo_inicial,
        tempo_camera,
        tempo_copia,
        tempo_warp,
        tempo_corte,
        tempo_hsv,
        tempo_centroids,
        tempo_centros,
        tempo_final,
    ):
        total = 100.0 / (tempo_final - tempo_inicial)
        print(
            Style.BRIGHT
            + "FRAME "
            + str(i_frame)
            + Style.NORMAL
            + "\nCâmera:  {0:.4f}s [{1:5.2f}%]\tCopia: {2:.4f}s [{3:5.2f}%]\t\tWarp: {4:.4f}s [{5:5.2f}%]\t\tCorte: {6:.4f}s [{7:5.2f}%]\nHSV:\t {8:.4f}s [{9:5.2f}%]\tCentroids: {10:.4f}s [{11:5.2f}%]\tCentros: {12:.4f}s [{13:5.2f}%]\n".format(
                tempo_camera - tempo_inicial,
                (tempo_camera - tempo_inicial) * total,
                tempo_copia - tempo_camera,
                (tempo_copia - tempo_camera) * total,
                tempo_warp - tempo_copia,
                (tempo_warp - tempo_copia) * total,
                tempo_corte - tempo_warp,
                (tempo_corte - tempo_warp) * total,
                tempo_hsv - tempo_corte,
                (tempo_hsv - tempo_corte) * total,
                tempo_centroids - tempo_hsv,
                (tempo_centroids - tempo_hsv) * total,
                tempo_centros - tempo_centroids,
                (tempo_centros - tempo_centroids) * total,
            )
            + Style.BRIGHT
            + "Total: {0:.4f}s  {1:.0f}ms\t\tFPS: {2:.4f}\n".format(
                tempo_final - tempo_inicial,
                1000.0 * (tempo_final - tempo_inicial),
                1.0 / (tempo_final - tempo_inicial),
            )
            + Style.NORMAL
        )
