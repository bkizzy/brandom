```mermaid
flowchart TD

  %% Entry Point
  A[App Installed] --> B{User Subscribed?}

  %% Abandonment Path
  B -- No --> C1[📲 Provisional Push (1h Post-Session)]
  C1 --> C2[📩 Reminder Email (1h Post-Session)]
  C2 --> C3[📲 Provisional Push 1 - 24h]
  C3 --> C4[📩 Reminder Email 1 - 24h]
  C4 --> C5[📲 Provisional Push 2 - 48h]
  C5 --> C6[📩 Reminder Email 2 - 72h]

  %% Subscription Path
  B -- Yes --> D1[📩 Welcome Email (Immediately)]
  D1 --> D2[📩 Progress Reminder Email (Day 3)]

  %% Habit Loop
  D2 --> E{User Activity?}
  E -- Streak --> F1[📲 Push: You’re on a streak! 💪]
  E -- Comeback --> F2[📲 Push: Let’s bounce back 🔁]
  E -- New/Restart --> F3[📲 Push: Let’s get started 💪]
  E -- No Workout --> F4[📲 Push: Log your activity 📝]

  %% Cancellation
  E --> G{User Cancelled?}
  G -- Yes --> H1[📲 Push: 1h Post-Cancel Win-Back 🔁]
  H1 --> H2[📩 Email: 1h Post-Cancel Win-Back]
  H2 --> H3[📲 Push: Win-Back (3 Days)]
  H3 --> H4[📩 Email: Win-Back (3 Days)]
  H4 --> H5[📲 Push: Win-Back (7 Days)]
  H5 --> H6[📩 Email: Win-Back (7 Days)]

  %% Re-subscribe possible endpoint
  H6 --> I{User Re-subscribed?}
  I -- Yes --> D1
  I -- No --> H6

```
