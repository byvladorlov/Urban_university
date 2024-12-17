def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function()
inner_function() #вызов этой функции невозможен, так как у «inner_function» будет локальное пространство,
# и «test_function» будет объемлющей для функции «inner_function»

