# img_process

This implement some tools to manipulate images. <br>
Work in progress to implement many tools. <br>

## uv

Use uv for dependency management:
Run the following command to install dependency.
```'(shell)
uv sync
```

## Concatenator

This tool is used to concatenate image into mosaic. <br>
It take several parameters in yaml file : crop, thin, border, etc. <br>

```(shell)
uv run ./concatenator.py -y yml/concatenator_op_cover_100_lq.yml
```

Example of output : <br>
![image](https://github.com/user-attachments/assets/6a0dc2cb-6d48-4b90-a162-3f08918fe70d)

## Note for github actions

Every yml files in .github/workflows generate an action.
In Settings->Actions->General activate "Read and write permissions" for workflow.
Also in Settings->Pages set the deployment from "gh-pages" "/(root)".
Site is here: https://leonmariotto.github.io/img_process/
