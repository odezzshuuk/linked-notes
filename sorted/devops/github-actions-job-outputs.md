# Github Actions - Job's Output

```yaml
jobs:
  # job1: the job that generates the output
  job1:
    runs-on: ubuntu-latest
    # Where to define the output of a job
    outputs:
      # Define Output name with {{ jobs.<job_id>.outputs.<output_name> }}
      output1: ${{ steps.step1.outputs.firstword }}
      output2: ${{ steps.step2.outputs.secondword }}
    steps: 
      - id: step1
        # echo "variable_name=value" >> $GITHUB_OUTPUT to set the output of a step
        run: echo "firstword=hello" >> $GITHUB_OUTPUT
      - id: step2
        run: echo "secondword=world" >> $GITHUB_OUTPUT
  # job2: the job that consumes the output of job1
  job2:
    runs-on: ubuntu-latest
    needs: job1 # job2 depends on job1, so it can access job1
    steps:
      - run: echo ${{ needs.job1.outputs.output1 }} \
             ${{ needs.job1.outputs.output2 }}
```

Define the output

- `jobs.<job_id>.outputs:` to define the output of a job
- `{{ jobs.<job_id>.outputs.<output_name> }}` to access the output of a job
- `echo "variable_name=value" >> $GITHUB_OUTPUT` to set the output of

Consume the output

- `jobs.<job_id>.needs:` to access the reusable workflow
- `outputs` consumed by expression `${{ needs.<job_id>.outputs.<output_name> }}`

