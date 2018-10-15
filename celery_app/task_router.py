class TaskRouter:
    def route_for_task(self, task, *args, **kwargs):
        namespace = 'default'
        if ':' in task:
            namespace, _ = task.split(':')

        print(">>>", task, namespace)

        return {'queue': namespace}