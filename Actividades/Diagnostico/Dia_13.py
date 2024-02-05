import ast
import graphviz

def dibujar_arbol(expr):
    nodo = ast.parse(expr, mode='eval')

    def visitar(nodo, grafo, padre=None):
        nombre = str(id(nodo))
        grafo.node(nombre, label=type(nodo).__name__)
        if padre is not None:
            grafo.edge(padre, nombre)
        for campo, valor in ast.iter_fields(nodo):
            if isinstance(valor, list):
                for item in valor:
                    if isinstance(item, ast.AST):
                        visitar(item, grafo, nombre)
            elif isinstance(valor, ast.AST):
                visitar(valor, grafo, nombre)

    grafo = graphviz.Digraph()
    visitar(nodo, grafo)
    return grafo

# Dibujar los árboles sintácticos
dibujar_arbol('1+2+3+4')
dibujar_arbol('1-2-3-4')
dibujar_arbol('1-(2-(3-4) + 1)')
