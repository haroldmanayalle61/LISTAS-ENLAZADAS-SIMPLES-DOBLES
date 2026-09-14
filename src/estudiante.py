class Estudiante:
    
    #Representa a un estudiante dentro del módulo académico

    def __init__(self, codigo: str, apellidos: str, nombres: str,
                 carrera: str, ciclo: int, promedio: float):
        self.codigo = codigo
        self.apellidos = apellidos
        self.nombres = nombres
        self.carrera = carrera
        self.ciclo = self._validar_ciclo(ciclo)
        self.promedio = self._validar_promedio(promedio)

    # ------------------------------------------------------------------
    # Validaciones 
    # ------------------------------------------------------------------
    @staticmethod
    def _validar_ciclo(ciclo: int) -> int:
        if not isinstance(ciclo, int) or ciclo <= 0:
            raise ValueError("El ciclo debe ser un número entero positivo.")
        return ciclo

    @staticmethod
    def _validar_promedio(promedio: float|int) -> float:
        if not isinstance(promedio, (int, float)) or not (0 <= promedio <= 20):
            raise ValueError("El promedio debe ser un número entre 0 y 20.")
        return float(promedio)

    def __str__(self)->str:
        return (f"[{self._codigo}] {self._apellidos}, {self._nombres} | "
                f"Carrera: {self._carrera} | Ciclo: {self._ciclo} | "
                f"Promedio: {self._promedio:.2f}")

    # ------------------------------------------------------------------
    # GETTERS Y SETTERS
    # ------------------------------------------------------------------
    @property
    def codigo(self) -> str:
        return self.__codigo

    @codigo.setter
    def codigo(self, nuevo_codigo: str):
        if not isinstance(nuevo_codigo, str) or not nuevo_codigo.strip():
            raise ValueError("El código debe ser una cadena de texto no vacía.")
        self._codigo = nuevo_codigo

    @property
    def apellidos(self) -> str:
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, nuevos_apellidos: str):
        self.__apellidos = nuevos_apellidos

    @property
    def nombres(self) -> str:
        return self.__nombres

    @nombres.setter
    def nombres(self, nuevos_nombres: str):
        self.__nombres = nuevos_nombres

    @property
    def carrera(self) -> str:
        return self.__carrera

    @carrera.setter
    def carrera(self, nueva_carrera: str):
        self.__carrera = nueva_carrera

    @property
    def ciclo(self) -> int:
        return self.__ciclo

    @ciclo.setter
    def ciclo(self, nuevo_ciclo: int):
        self.__ciclo = self._validar_ciclo(nuevo_ciclo)

    @property
    def promedio(self) -> float:
        return self.__promedio

    @promedio.setter
    def promedio(self, nuevo_promedio: float):
        self.__promedio = self._validar_promedio(nuevo_promedio)

