from graphviz import Digraph

# Vytvoření UseCase diagramu
diagram = Digraph('UseCaseDiagram', format='png')
diagram.attr(rankdir='LR', size='8,5')

# Přidání aktérů
diagram.node('Z', 'Zákazník', shape='ellipse', style='filled', color='lightblue')
diagram.node('A', 'Administrátor', shape='ellipse', style='filled', color='lightgreen')
diagram.node('P', 'Prodejce', shape='ellipse', style='filled', color='lightyellow')
diagram.node('PS', 'Platební systém', shape='ellipse', style='filled', color='pink')
diagram.node('DS', 'Doručovací služba', shape='ellipse', style='filled', color='orange')

# Přidání případů užití
diagram.node('R', 'Registrace a přihlášení', shape='box')
diagram.node('B', 'Prohlížení produktů', shape='box')
diagram.node('O', 'Vytvoření objednávky', shape='box')
diagram.node('SP', 'Správa produktů', shape='box')
diagram.node('SM', 'Správa skladových zásob', shape='box')
diagram.node('PZ', 'Zpracování plateb', shape='box')
diagram.node('SD', 'Sledování doručení', shape='box')

# Spojení aktérů a případů užití
diagram.edges([
    ('Z', 'R'),  # Zákazník -> Registrace a přihlášení
    ('Z', 'B'),  # Zákazník -> Prohlížení produktů
    ('Z', 'O'),  # Zákazník -> Vytvoření objednávky
    ('A', 'SP'), # Administrátor -> Správa produktů
    ('A', 'SM'), # Administrátor -> Správa skladových zásob
    ('P', 'SM'), # Prodejce -> Správa skladových zásob
    ('O', 'PZ'), # Vytvoření objednávky -> Zpracování plateb
    ('PZ', 'PS'),# Zpracování plateb -> Platební systém
    ('O', 'SD'), # Vytvoření objednávky -> Sledování doručení
    ('SD', 'DS') # Sledování doručení -> Doručovací služba
])

# Uložení a vykreslení diagramu
diagram_filepath = '/mnt/data/UseCaseDiagram_eShop.png'
diagram.render(diagram_filepath, cleanup=True)
diagram_filepath
