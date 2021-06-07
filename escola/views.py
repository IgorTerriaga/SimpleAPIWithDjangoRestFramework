from rest_framework import serializers, viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import (
    AlunoSerializer,
    CursoSerializer,
    MatriculaSerializer,
    ListaMatriculasAlunoSerializer,
)


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matriculas"""

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um alun@"""
    def get_queryset(self):
        """ filtrando pelo id do aluno """
        queryset = Matricula.objects.filter(aluno_id=self.kwargs["pk"])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
