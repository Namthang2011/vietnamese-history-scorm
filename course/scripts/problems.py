from dataclasses import dataclass
from typing import Literal


@dataclass
class Problem:
    description: str
    right_answer: Literal["a", "b", "c", "d"]

    a: str
    b: str
    c: str
    d: str


problems = [
    Problem(
        description="Liên quân Pháp - Tây Ban Nha nổ súng đánh vào cửa biển Đà Nẵng vào ngày tháng năm nào?",
        right_answer="b",
        a="09-01-1858",
        b="01-09-1858",
        c="09-01-1859",
        d="01-09-1859",
    ),
    Problem(
        description="Hiệp ước cuối cùng, đánh dấu sự đầu hàng hoàn toàn của triều đình phong kiến nước ta trước thế lực xâm lăng, kết thúc giai đoạn tồn tại của Nhà nước phong kiến Việt Nam độc lập là Hiệp ước nào",
        right_answer="d",
        a="Nhâm Tuất",
        b="Giáp Tuất",
        c="Harmand",
        d="Patơnốt",
    ),
    Problem(
        description="Nhân vật chủ chốt trong Phong trào Đông Du là ai?",
        right_answer="a",
        a="Phan Bội Châu",
        b="Phan Châu Trinh",
        c="Nguyễn Tất Thành",
        d="Tôn Thất Thuyết",
    ),
    Problem(
        description="Cuộc khai thác thuộc địa lần thứ hai của Thực dân Pháp ở nước ta diễn ra trong khoảng thời gian nào?",
        right_answer="c",
        a="1917-1927",
        b="1918-1927",
        c="1919-1929",
        d="1919-1928",
    ),
    Problem(
        description="Đảng Cộng sản Việt Nam ra đời năm nào?",
        right_answer="d",
        a="1927",
        b="1928",
        c="1929",
        d="1930",
    ),
    Problem(
        description="Phong trào Xô viết Nghệ Tĩnh diễn ra vào năm nào?",
        right_answer="c",
        a="1928-1930",
        b="1929-1930",
        c="1930-1931",
        d="1930-1932",
    ),
    Problem(
        description="Nguyễn Ái Quốc về nước trực tiếp lãnh đạo cách mạng từ năm nào?",
        right_answer="b",
        a="1940",
        b="1941",
        c="1939",
        d="1942",
    ),
    Problem(
        description="Sau khi nước Việt Nam Dân chủ Cộng hoà được thành lập, trong tình hình đất nước gặp muôn vàn khó khăn thử thách, nhân dân ta vừa xây dựng chính quyền cách mạng, vừa phải diệt giặc nào?",
        right_answer="d",
        a="Giặc đói",
        b="Giặc dốt",
        c="Giặc ngoại xâm",
        d="Cả 3 giặc trên",
    ),
    Problem(
        description="Chiến dịch Việt Bắc diễn ra vào năm nào?",
        right_answer="a",
        a="1947",
        b="1948",
        c="1949",
        d="1950",
    ),
    Problem(
        description="Chiến dịch cuối cùng đánh bại Thực dân Pháp, khiến chúng hoàn toàn rời khỏi Việt Nam là chiến dịch nào?",
        right_answer="b",
        a="Chiến dịch Việt Bắc",
        b="Chiến dịch Điện Biên Phủ",
        c="Chiến dịch Biên Giới",
        d="Chiến dịch Hồ Chí Minh",
    ),
]
