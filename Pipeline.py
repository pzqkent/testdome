class Pipeline:
    @staticmethod
    def pipeline(*funcs):
        def helper(arg):
            for i in funcs:
                arg = i(arg)
            return arg


        return helper
    
fun = Pipeline.pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3)) #should print 5.0