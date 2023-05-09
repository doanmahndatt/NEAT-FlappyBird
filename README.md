# NEAT-FlappyBird
How to use NEAT in game Flappy Bird

[NEAT]
# Đây là tiêu chí đánh giá thể lực của các cá thể (hay genome) trong quần thể
fitness_criterion     = max
# Đây là ngưỡng thể lực tối thiểu mà một cá thể cần đạt được để được coi là thành công.
fitness_threshold     = 100
# Kích thước của quần thể ban đầu.
pop_size              = 70
# Xác định xem liệu việc giết hết các cá thể trong một thế hệ có dẫn đến việc khởi tạo một quần thể mới không.
reset_on_extinction   = False

[DefaultGenome]
# Hoạt động của node
# giá trị mặc định của hàm kích hoạt cho một node (tanh trong trường hợp này).
activation_default      = tanh
# tỷ lệ đột biến của hàm kích hoạt cho node.
activation_mutate_rate  = 0.0
#  các tùy chọn hàm kích hoạt khả dĩ cho node
activation_options      = tanh

# node aggregation options
# Chọn cách thức tính toán giá trị đầu ra của các nút dựa trên giá trị đầu vào của chúng, ở đây là "sum"
aggregation_default     = sum
#  Tỉ lệ thay đổi ngẫu nhiên cách thức tính toán giá trị đầu ra của các nút trong quá trình tiến hóa genome.
aggregation_mutate_rate = 0.0
# Danh sách các phương thức tính toán giá trị đầu ra của các nút, ở đây chỉ có "sum".
aggregation_options     = sum

# node bias options
# Giá trị trung bình ban đầu của bias (độ lệch) của các nút.
bias_init_mean          = 0.0
# Độ lệch chuẩn ban đầu của bias của các nút.
bias_init_stdev         = 1.0
# Giá trị tối đa cho bias của các nút.
bias_max_value          = 30.0
# Giá trị tối thiểu cho bias của các nút.
bias_min_value          = -30.0
#  Mức độ ảnh hưởng của quá trình đột biến đến giá trị bias của các nút.
bias_mutate_power       = 0.5
#  Tỉ lệ đột biến bias của các nút trong quá trình tiến hóa genome.
bias_mutate_rate        = 0.7
# Tỉ lệ thay thế bias của các nút trong quá trình tiến hóa genome.
bias_replace_rate       = 0.1

# genome compatibility options
# Hệ số đánh giá sự khác biệt trong cấu trúc của genome khi đo độ tương thích giữa các genome khác nhau trong quá trình lai ghép.
compatibility_disjoint_coefficient = 1.0
# Hệ số đánh giá sự khác biệt trong trọng số của genome khi đo độ tương thích giữa các genome khác nhau trong quá trình lai ghép.
compatibility_weight_coefficient   = 0.5

# connection add/remove rates
# xác suất để một kết nối mới được thêm vào giữa các nơ-ron trong một thế hệ mới.
conn_add_prob           = 0.5
# xác suất để một kết nối bị xóa khỏi một thế hệ.
conn_delete_prob        = 0.5

# connection enable options
# xác định trạng thái mặc định của kết nối mới được thêm vào: có kích hoạt hay không.
enabled_default         = True
# tỷ lệ thay đổi trạng thái của một kết nối từ được kích hoạt sang không kích hoạt hoặc ngược lại.
enabled_mutate_rate     = 0.01

# cờ đánh dấu xem mạng lưới có phải là mạng lưới truyền thẳng hay không.
feed_forward            = True
# chỉ định cách kết nối ban đầu giữa các nơ-ron.
initial_connection      = full

# node add/remove rates
# xác suất để một nơ-ron mới được thêm vào giữa các lớp trong một thế hệ.
node_add_prob           = 0.2
# xác suất để một nơ-ron bị xóa khỏi một thế hệ.
node_delete_prob        = 0.2

# network parameters
# chỉ định số lượng nơ-ron ẩn trong mạng.
num_hidden              = 0
# chỉ định số lượng nơ-ron đầu vào.
num_inputs              = 3
# chỉ định số lượng nơ-ron đầu ra.
num_outputs             = 1

# node response options
# giá trị trung bình ban đầu của phản hồi của một nơ-ron.
response_init_mean      = 1.0
# độ lệch chuẩn ban đầu của phản hồi của một nơ-ron.
response_init_stdev     = 0.0
# giá trị tối đa của phản hồi của một nơ-ron.
response_max_value      = 30.0
# giá trị tối thiểu của phản hồi của một nơ-ron.
response_min_value      = -30.0
# mức độ thay đổi giá trị phản hồi của một nơ-ron trong quá trình đột biến.
response_mutate_power   = 0.0
#  tỷ lệ đột biến giá trị phản hồi của một nơ-ron.
response_mutate_rate    = 0.0
# tỷ lệ thay thế giá trị phản hồi của một nơ-ron bằng giá trị mới.
response_replace_rate   = 0.0

# connection weight options
# giá trị trung bình ban đầu của trọng số kết nối, được khởi tạo ngẫu nhiên từ phân phối chuẩn với giá trị trung bình này.
weight_init_mean        = 0.0
# độ lệch chuẩn của phân phối khởi tạo trọng số kết nối.
weight_init_stdev       = 1.0
# giá trị lớn nhất có thể có cho trọng số kết nối.
weight_max_value        = 30
# giá trị nhỏ nhất có thể có cho trọng số kết nối.
weight_min_value        = -30
# độ mạnh của quá trình đột biến trọng số kết nối, được tính theo một phân phối Gauss với giá trị trung bình là 0 và độ lệch chuẩn là weight_mutate_power.
weight_mutate_power     = 0.5
# xác suất để một trọng số kết nối bị đột biến.
weight_mutate_rate      = 0.8
# xác suất để một trọng số kết nối bị thay thế bằng một giá trị ngẫu nhiên khác.
weight_replace_rate     = 0.1

# xác định ngưỡng tương thích để xác định xem hai cá thể có thuộc cùng một loài hay không.
# Nếu khoảng cách giữa các cá thể nhỏ hơn ngưỡng tương thích này, chúng sẽ thuộc cùng một loài trong quần thể.
[DefaultSpeciesSet]
compatibility_threshold = 3.0

# Để giải quyết vấn đề đình trệ trong quần thể, hệ thống sử dụng thông số max_stagnation để xác định số lượng thế hệ liên tiếp mà không có sự cải thiện nào trong tất cả các loài trong quần thể. Nếu quá trình tạo ra thế hệ mới không cải thiện được tình trạng đình trệ này, hệ thống sẽ loại bỏ các loài kém hiệu quả để giảm kích thước quần thể.
# species_elitism là số lượng cá thể ưu tú được giữ lại trong mỗi loài để đảm bảo tính đa dạng của quần thể
[DefaultStagnation]
species_fitness_func = max
max_stagnation       = 20
species_elitism      = 2

# Xác định cách tạo thế hệ mới từ thế hệ hiện tại của quần thể
[DefaultReproduction]
elitism            = 2
survival_threshold = 0.2
min_species_size = 2
