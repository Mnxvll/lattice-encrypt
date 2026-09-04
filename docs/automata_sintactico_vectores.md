# Autómata Sintáctico: Suma de Vectores

Este diagrama representa el autómata de validación gramatical (Sintáctico) para la regla: `VECTOR(a,b) SUMA VECTOR(c,d)`. En el analizador sintáctico, las transiciones ya no son caracteres (letras o números), sino **Tokens enteros** entregados por el analizador léxico.

## Componentes Básicos
*   **Estado Inicial (`q0`)**: Estado en el que el analizador empieza a evaluar la regla gramatical.
*   **Estados Intermedios (`q1` a `q12`)**: Estados que indican que la regla se está cumpliendo parcialmente, pero aún faltan tokens (piezas de la receta) por consumir.
*   **Estado de Aceptación (`q13`)**: (Doble círculo) Significa que toda la secuencia llegó exactamente en el orden esperado y la instrucción de suma de vectores es sintácticamente válida para ejecutarse.
*   **Transiciones**: Los consumos esperados. Por ejemplo, `self.consumir("PALABRA")` o `self.consumir("IPAREN")`.

## Diagrama 
```mermaid
graph TD
    %% Inicio
    start[ Inicio ] --> q0((q0))
    style start fill:none,stroke:none

    %% Primer vector
    q0 -->|"Token: PALABRA 'VECTOR'"| q1((q1))
    q1 -->|"Token: IPAREN '('"| q2((q2))
    q2 -->|"Token: NUMERO 'n1'"| q3((q3))
    q3 -->|"Token: COMA ','"| q4((q4))
    q4 -->|"Token: NUMERO 'n2'"| q5((q5))
    q5 -->|"Token: DPAREN ')'"| q6((q6))

    %% Operador matemático
    q6 -->|"Token: SUMA '+'"| q7((q7))

    %% Segundo vector
    q7 -->|"Token: PALABRA 'VECTOR'"| q8((q8))
    q8 -->|"Token: IPAREN '('"| q9((q9))
    q9 -->|"Token: NUMERO 'n3'"| q10((q10))
    q10 -->|"Token: COMA ','"| q11((q11))
    q11 -->|"Token: NUMERO 'n4'"| q12((q12))
    
    %% Fin / Aceptación
    q12 -->|"Token: DPAREN ')'"| q13(((q13)))
```

Si estando en el estado `q2` llega un token `PALABRA` en lugar de un `NUMERO`, el autómata no tiene una flecha válida por dónde avanzar y "crachea", lanzando el error (`SyntaxError: Se esperaba NUMERO y llegó PALABRA...`).
