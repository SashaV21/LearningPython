# Структурная схема алгоритма модели GPSS

```mermaid
graph TD
    A[НАЧАЛО] --> B[GENERATE 5,4<br>Новая заявка]
    B --> C{TEST E BV$Kont1,1<br>Очередь < 5?}
    C -->|Да| D[QUEUE RemQ<br>Добавить в очередь]
    C -->|Нет| E[TERMINATE<br>Отказ]
    D --> F{TRANSFER 0.500<br>Выбор грузовика}
    F -->|Грузовик 1| G[ADVANCE 1<br>Сеанс связи]
    F -->|Грузовик 2| H[ADVANCE 1<br>Сеанс связи]
    
    G --> I{TEST E BV$provrem1<br>Свободен?}
    I -->|Да| J[SEIZE Rem1<br>Захват]
    I -->|Нет| K[ADVANCE 1<br>Повторная попытка]
    J --> L[DEPART RemQ<br>Выход из очереди]
    L --> M[ADVANCE 12,8<br>Перевозка]
    M --> N[RELEASE Rem1<br>Освобождение]
    N --> O[TERMINATE<br>Учет]
    
    H --> P{TEST E BV$provrem2<br>Свободен?}
    P -->|Да| Q[SEIZE Rem2<br>Захват]
    P -->|Нет| R[ADVANCE 1<br>Повторная попытка]
    Q --> S[DEPART RemQ<br>Выход из очереди]
    S --> T[ADVANCE 12,8<br>Перевозка]
    T --> U[RELEASE Rem2<br>Освобождение]
    U --> V[TERMINATE<br>Учет]
    
    K --> F
    R --> F
    
    style A fill:#9f9,stroke:#333
    style E fill:#f99,stroke:#333
    style O fill:#99f,stroke:#333
    style V fill:#99f,stroke:#333
