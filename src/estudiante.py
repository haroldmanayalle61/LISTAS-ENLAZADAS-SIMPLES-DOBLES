class Estudiante:
    
    #Representa a un estudiante dentro del módulo académico

    def __init__(self, codigo: str, apellidos: str, nombres: str,
                 carrera: str, ciclo: int, promedio: float):
        self.codigo = codigo
        self.apellidos = apellidos
        self.nombres = nombres
        self.carrera = carrera
        self.ciclo = ciclo
        self.promedio = promedio

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

    @staticmethod
    def _validar_cadena(cadena:str)->str:
        if not isinstance(cadena, str):
            raise ValueError("Nombres, apellidos y carrera deben ser una cadena de texto.")

        cadena = cadena.strip()

        if not cadena:
            raise ValueError("Nombres, apellidos y carrera no pueden estar vacío.")

        for caracter in cadena:
            if not (caracter.isalpha() or caracter == " "):
                raise ValueError("Nombres, apellidos y carrera solo pueden contener letras y espacios.")
        return cadena

    def __str__(self)->str:
        return (f"[{self.__codigo}] {self.__apellidos}, {self.__nombres} | "
                f"Carrera: {self.__carrera} | Ciclo: {self.__ciclo} | "
                f"Promedio: {self.__promedio:.2f}")

    # ------------------------------------------------------------------
    # GETTERS Y SETTERS
    # ------------------------------------------------------------------
    @property
    def codigo(self) -> str:
        return self.__codigo

    @codigo.setter
    def codigo(self, nuevo_codigo: str):
        if not isinstance(nuevo_codigo, str):
            raise ValueError("El código debe ser una cadena de texto.")

        nuevo_codigo = nuevo_codigo.strip()

        if not nuevo_codigo:
            raise ValueError("El código no puede estar vacío.")

        if not nuevo_codigo.isalnum():
            raise ValueError("El código solo puede contener letras y dígitos.")

        self.__codigo = nuevo_codigo

    @property
    def apellidos(self) -> str:
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, nuevos_apellidos: str):
        self.__apellidos = self._validar_cadena(nuevos_apellidos)

    @property
    def nombres(self) -> str:
        return self.__nombres

    @nombres.setter
    def nombres(self, nuevos_nombres: str):
        self.__nombres = self._validar_cadena(nuevos_nombres)

    @property
    def carrera(self) -> str:
        return self.__carrera

    @carrera.setter
    def carrera(self, nueva_carrera: str):
        self.__carrera = self._validar_cadena(nueva_carrera)

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

