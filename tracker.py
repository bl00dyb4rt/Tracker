#!/usr/bin/python
import subprocess
import argparse


class Tracker:
    def __init__(self):
        self.arguments()

    def arguments(self):
        repo_parse = argparse.ArgumentParser(description='Tracking RPM\'s', add_help=False)

        repo_parse.add_argument('-d', '--directory', dest='directory', action='store',
                                help='Directorio en donde se generará el repositorio')
        repo_parse.add_argument('-p', '--package', dest='package', action='store',
                                help='Nombre del paquete a descargar')

        args = repo_parse.parse_args()
        directory = str(args.directory)
        full_path = self.get_full_path(directory)

        name_repository = 'repository'
        directory_rep = full_path + name_repository
        package = str(args.package)
        # usando repotrack
        self.repotrack(directory_rep, package)
        nametar = package + '.tar.gz'

        # generando el repositorio
        self.createrepo(directory_rep)

        # comprimiendo
        self.tar_directory(full_path, nametar, name_repository)
        # moviendo
        self.moviendo(full_path, nametar)
        subprocess.run(['echo', 'Completado....! \n'])

    def repotrack(self, directory, package):

        text = "+-+-+-+-+-+ +-+-+-+-+-+ \n" \
               + "|T|r|a|c|k||e||r| |by| |B|4|r|t|\n" \
               + "+-+-+-+-+-+ +-+-+-+-+-+\n"
        subprocess.run(['echo', text])
        subprocess.run(['echo', 'Iniciando Repotrack \n'])
        subprocess.run(['repotrack', '-p' + directory, package])

    def tar_directory(self, full_path, name_tar, name_directory_tar):
        subprocess.run(['echo', 'Comprimiendo \n'])
        subprocess.run(['tar', '-zcvf', name_tar, '-C', full_path, name_directory_tar])
        subprocess.run(['echo', '\n'])

    def get_full_path(self, path):

        split_dir = path.split('/')

        if split_dir[len(split_dir) - 1] == '':
            full_path = path
        else:
            full_path = path + '/'

        return full_path

    def createrepo(self, path_repo):
        subprocess.run(['echo', 'Creando el Repositorio \n'])
        subprocess.run(['createrepo', path_repo])
        subprocess.run(['echo', '\n'])

    def moviendo(self, full_path, name):
        subprocess.run(['echo', 'Moviendo tar al directorio \n'])
        subprocess.run(['mv', name, full_path])
        subprocess.run(['echo', '\n'])


Tracker()
