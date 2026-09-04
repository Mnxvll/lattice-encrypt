# Diagrama de Secuencia

Este diagrama muestra el flujo de ejecución paso a paso desde que el usuario ingresa un comando hasta que se imprime el resultado, utilizando como ejemplo la operación `VECTOR(1,2) SUMA VECTOR(3,4)`.

```mermaid
sequenceDiagram
    participant U as Usuario
    participant R as Runner
    participant L as Lexico
    participant S as Sintactico
    participant J as reglas.json
    participant B as ReglasBase

    U->>R: Escribe: "VECTOR(1,2) SUMA VECTOR(3,4)"
    
    Note over R,L: Fase Léxica
    R->>L: tokenizar("VECTOR...")
    L-->>R: [Token(PALABRA, "VECTOR"), Token(IPAREN, "("), ...]
    
    Note over R,S: Fase Sintáctica y Despacho
    R->>S: analisisSintactico(tokens)
    
    S->>S: parsear_vector() -> Retorna (1.0, 2.0)
    S->>S: consumir(PALABRA) -> "SUMA"
    
    S->>J: Buscar "SUMA" en grupos
    J-->>S: Encuentra "SUMA" -> Archivo: "ReglasBase", Regla: "revisarSintaxisBase"
    
    Note over S,B: Carga Dinámica e Inyección de Dependencia
    S->>B: importlib.import_module("reglas.ReglasBase")
    S->>B: revisarSintaxisBase(Sintactico, (1.0, 2.0), "SUMA")
    
    B->>S: sintactico.consumir(PALABRA) -> "VECTOR"
    B->>S: sintactico.parsear_vector() -> Retorna (1.0, 2.0)+(3.0, 4.0)
    
    Note over B: Ejecución Matemática
    B->>B: Suma tuplas: (1.0+3.0, 2.0+4.0)
    B-->>S: Retorna resultado (4.0, 6.0)
    
    S-->>R: Retorna resultado (4.0, 6.0)
    R-->>U: Imprime "Resultado: (4.0, 6.0)"
```
