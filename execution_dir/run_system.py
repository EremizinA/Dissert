from subprocess import call

file1 = open('/home/alex/PycharmProjects/dis/examples/adder.sh', 'rb').read()

obj_dump = "objdump"
preffix = "-d"
dir_path = "/home/alex/PycharmProjects/dis/examples/"
exec_filenames = ["example1", "example2", "example3"]

disasemble_results = list()

for filename in exec_filenames:
    disasemble_results.append(call([obj_dump, preffix, dir_path + filename]))


