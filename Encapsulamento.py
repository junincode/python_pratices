# The command object.setatt(_attribute , _value) works to access the attributes and putting a new value.
# The command object.getattribute(_attribute) works to obtain the attributes' value called.
class ControleRemoto:

    menu = bool

    # ATRIBUTOS.
    def __init__(self, volume=50, ligado=True, tocando=False):
        self.__volume = volume
        self.ligado = ligado
        self.tocando = tocando

    # GETTERS E SETTERS.
    @property
    def volume(self):
       # print("Getter em andamento")
        return self._volume

    @volume.setter
    def volume(self, volume):
        if not isinstance(volume, int):
            raise ValueError("O valor de 'volume' deve ser do tipo inteiro.")
        else:
            self._volume = volume

    @property
    def ligado(self):
       # print("Getter em andamento")
        return self._ligado

    @ligado.setter
    def ligado(self, ligado):
        if not isinstance(ligado, bool):
            raise ValueError("O valor deve ser do tipo VERDADEIRO/FALSO")
        else:
            self._ligado = ligado

    @property
    def tocando(self):
       # print("Getter em andamento")
        return self._tocando

    @tocando.setter
    def tocando(self, tocando):
        if not isinstance(tocando, bool):
            raise ValueError("O valor para 'tocando' deve ser do tipo VERDADEIRO/FALSO")
        else:
            self._tocando = tocando

    @property
    def menu(self):
        return self._menu

    @menu.setter
    def menu(self, menu):
        if not isinstance(menu, bool):
            raise("O valor para 'menu' deve ser do tipo VERDADEIRO/FALSO.")
        else:
            self._menu = menu

    # MÉTODOS.
    def describe(self):
        print(f"Volume = {self.volume}")
        print(f"Está ligado = {self.ligado}")
        print(f"Está tocando = {self.tocando}")

    def ligar(self):
        self.volume = True
        print("O controle está ligado.")

    def desligar(self):
        self.ligado = False
        print("O controle está desligado.")

    def abrir_menu(self):
        if self.ligado == False:
            print("Impossível abrir o menu com o controle desligado.")
        else:
            print("Menu aberto.")

    def fechar_menu(self):
        if self.ligado == False:
            print("Impossível fechar o menu com o controle desligado.")
        elif self.menu == False:
            print("O menu já está fechado.")
        else:
            print("Menu fechado.")

    def mais_volume(self, aumenta):
        if not isinstance(aumenta, int):
            raise ValueError("O valor para volume deve ser do tipo INTEIRO.")
        if aumenta < 0:
            print(f"O controle não aceita valores negativo como {aumenta}")
        else:
            self.volume += aumenta
            if self.volume > 100:
                self.volume = 100

    def menos_volume(self, diminui):
        global antigo
        if not isinstance(diminui, int):
            raise ValueError("O valor para volume deve ser do tipo INTEIRO.")
        if diminui < 0:
            print(f"O controle não aceita valores negativos como {diminui}")
        else:
            self.volume -= diminui
            if self.volume < 0:
                antigo = self.volume + diminui
                self.volume = 0

    def ligar_mudo(self):
        global antigo
        if self.volume == 0:
            print("O volume já está no mudo.")
        else:
            antigo = self.volume
            self.volume = 0
            print("Volume mudo.")

    def desligar_mudo(self):
        if self.volume != 0:
            print("O volume já não está no mudo.")
        else:
            self.volume = antigo

    def play(self):
        self.tocando = True
        print("Está tocando.")

    def pause(self):
        self.tocando = False
        print("Está pausado.")


c1 = ControleRemoto()
