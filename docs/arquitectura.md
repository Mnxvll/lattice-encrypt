# Arquitectura del Intérprete Lattice Encrypt

Este diagrama describe la arquitectura general del proyecto, mostrando cómo se conectan los módulos principales y el despachador dinámico. Utilizando como ejemplo la operación `VECTOR(1,2) SUMA VECTOR(3,4)`.

```mermaid
graph TD
    %% Estilos
    classDef user fill:#FFDDC1,stroke:#333,stroke-width:2px,color:black;
    classDef core fill:#D4F0F0,stroke:#333,stroke-width:2px,color:black;
    classDef json fill:#C8E6C9,stroke:#333,stroke-width:2px,color:black;
    classDef plugin fill:#E1BEE7,stroke:#333,stroke-width:2px,color:black;

    %% Nodos Principales
    U(( Usuario / Consola)):::user
    R[ Runner.py<br>Punto de Entrada]:::core
    L[ LatticeLexico.py<br>Analizador Léxico]:::core
    S[ LatticeSintactico.py<br>Despachador Dinámico]:::core
    J[( reglas.json)]:::json

    %% Carpeta de reglas
    subgraph "Plugins Matemáticos"
        direction LR
        RB[ReglasBase.py]:::plugin
        RR[ReglasRuido.py]:::plugin
        RT[ReglasTexto.py]:::plugin
        RL[ReglasLattice.py]:::plugin
    end

    %% Relaciones
    U -- "1. Escribe Comando" --> R
    R -- "2. Texto" --> L
    L -- "3. Tokens" --> R
    R -- "4. Envía Tokens" --> S
    
    S -- "5. Lee Configuración" --> J
    J -. "Indica archivo a importar" .-> S

    S -- "6. Importa y Ejecuta" --> RB
    S -- "6. Importa y Ejecuta" --> RR
    S -- "6. Importa y Ejecuta" --> RT
    S -- "6. Importa y Ejecuta" --> RL

    RB -. "7. Retorna cálculo" .-> S
    S -. "8. Resultado" .-> R
    R -. "9. Imprime consola" .-> U
```
