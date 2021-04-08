class swift:
    def start(self):
        print("swift start method")
    def accelerate(self):
        print("swift accelerate method")
    def stop(self):
        print("swift stop")

class seltos:
    def start(self):
        print("seltos start method")
    def accelerate(self):
        print("seltos accelerate method")
    def stop(self):
        print("seltos stop")

class person:
    def drive(self,car):
        car.start()
        car.accelerate()
        car.stop()

sw=swift()
p=person()
p.drive(sw)

######################################################


class pycharm:
    def create_file(self):
        print("create a file pycharm")
    def execute_file(self):
        print("execute of pycharm")
class vscode:
    def create_file(self):
        print("create a file vscode")
class programmer:
    def coding(self,ide):
        ide.create_file()
        ide.execute_file()

cd=pycharm()
pg=programmer()
pg.coding(cd)



