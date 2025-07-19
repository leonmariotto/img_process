from scripts.ImgTool import ImgTool


def test_load_save():
    imgtool = ImgTool()
    img_content = imgtool.load("images/op_covers/cover_T001.jpg")
    assert img_content.shape == (3005, 1920, 3)
