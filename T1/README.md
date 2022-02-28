# HOW TO RUN

client: `py client.py <protocol> <filename> <buffer_size> <ack>`
server: `py server.py <protocol> <buffer_size> <ack>`

`<protocol>: udp or tcp`
`<ack>: true or false`

# Results

### TCP

| ACK | NR. OF TRIES | SIZE  | BUFFER SIZE | PKS SEND | PKS RECEIVED | % LOSS (Avg.) | TIME (Avg.) |
| :-: | :----------: | :---: | :---------: | :------: | :----------: | :-----------: | :---------: |
| NO  |      50      | 100MB |   1024 B    |  102830  |    102830    |      0%       |   0.169s    |
| NO  |      10      |  1GB  |   1024 B    |  978664  |    978664    |      0%       |   1.683s    |
| NO  |      10      |  1GB  |   8096 B    |  123784  |    123784    |      0%       |    0.42s    |
| NO  |      10      |  1GB  |   16192 B   |  61892   |    61892     |      0%       |    0.16s    |
| YES |      50      | 100MB |   1024 B    |  102830  |    102830    |      0%       |    1.96s    |
| YES |      10      |  1GB  |   1024 B    |  978664  |    978664    |      0%       |    17.6s    |

### UDP

| ACK | NR. OF TRIES | SIZE  | BUFFER SIZE | PKS SEND | PKS RECEIVED | % LOSS (Avg.) | TIME (Avg.) |
| :-: | :----------: | :---: | :---------: | :------: | :----------: | :-----------: | :---------: |
| NO  |      50      | 100MB |   1024 B    |  102830  |    96079     |     6.56%     |   0.231s    |
| NO  |      10      |  1GB  |   1024 B    |  978664  |    954465    |     2.47%     |    2.24s    |
| NO  |      10      |  1GB  |   8096 B    |  123784  |    123395    |     0.31%     |    0.49s    |
| NO  |      -       |   -   |   16192 B   |    -     |      -       |       -       |      -      |
| YES |      50      | 100MB |   1024 B    |  102830  |    102830    |      0%       |    1.81s    |
| YES |      10      |  1GB  |   1024 B    |  978664  |    978664    |      0%       |    16.9s    |
