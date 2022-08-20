from random import randint


class RefractorTelecsope:
    def __init__(self, code):
        self.code = code
        self.lens = None
        self.mirror = None
        self.camera = None

    def __str__(self):
        return f"""
            Refractor telecsope 'Aurora'
            product number: {self.code}
            lens: {self.lens}
            mirror: {self.mirror}
            camera: {self.camera if self.camera else "abscence"}
        """


class ReflectorTelecsope:
    def __init__(self, code,):
        self.code = code
        self.first_lens = None
        self.second_lens = None
        self.camera = None

    def __str__(self):
        return f"""
            Reflector telecsope 'Cassiopeia'
            product number: {self.code}
            lens: {self.first_lens} and {self.second_lens}
            camera: {self.camera}
        """


class RefractorTelecsopeBuilder:
    def __init__(self):
        self.telecope = RefractorTelecsope(randint(10000, 99000))

    def install_lens(self, lens):
        self.telecope.lens = lens

    def install_camera(self, camera):
        self.telecope.camera = camera

    def install_mirror(self, mirror):
        self.telecope.mirror = mirror


class ReflectorTelecsopeBuilder:
    def __init__(self):
        self.telecope = ReflectorTelecsope(randint(10000, 99000))

    def install_first_lens(self, first_lens):
        self.telecope.first_lens = first_lens

    def install_second_lens(self, second_lens):
        self.telecope.second_lens = second_lens

    def install_camera(self, camera):
        self.telecope.camera = cameramirror


class Engineer:
    def __init__(self):
        self.builder = None

    def build_refractor_telecope_with_camere(self):
        self.builder = RefractorTelecsopeBuilder()

        self.builder.install_lens("4x Superior")
        self.builder.install_mirror("4.5 Phabula")
        self.builder.install_camera("Cannon Inteligance")

    def build_refractor_telecope_without_camera(self):
        self.builder = RefractorTelecsopeBuilder()

        self.builder.install_lens("4x Superior")
        self.builder.install_mirror("4.5 Phabula")

    @property
    def telecope(self):
        telecope = self.builder.telecope
        self.builder.telecope = None
        return telecope


engineer = Engineer()

engineer.build_refractor_telecope_with_camere()
print(engineer.telecope)

engineer.build_refractor_telecope_without_camera()
print(engineer.telecope)
