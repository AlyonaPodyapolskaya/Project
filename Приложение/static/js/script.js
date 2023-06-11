var from = document.getElementById('from');
var to = document.getElementById('to');
var ctgr = document.getElementById('categoties');
var ipf = document.getElementById('ipf');
var ipt = document.getElementById('ipt');
var input = document.getElementById('input');
var result = document.getElementById('result');

var lenght_list = ["Километр", "Метр", "Сантиметр", "Миллиметр", "Микрометр", "Нанометр", "Миля", "Ярд", "Фут", "Дюйм", "Морская миля"]
var time_list = ["Наносекунда", "Микросекунда", "Миллисекунда", "Секунда", "Минута", "Час", "День", "Неделя",
"Месяц", "Год", "Десятилетие", "Век"]
var pressure_list = ["Атмосфера", "Бар", "Паскаль", "Topp", "Фунт-сила на квадратный дюйм"]
var mass_list = ["Тонна", "Килограмм", "Грамм", "Миллиграмм", "Микрограмм", "Стоун", "Фунт", "Унция"]
var volume_list = ["Кубический метр", "Литр", "Миллилитр", "Кубический фут", "Кубический дюйм"]
var square_list = ["Квадратный метр", "Квадратный километр", "Квадратная миля", "Квадратный ярд", "Квадратный фут", "Квадратный дюйм", "Гектар", "Акр"]
var speed_list = ["Миля в час", "Фут в секунду", "Метр в секунду", "Километр в час"]

var temperature_list = ["Градус Цельсия", "Градус Фаренгейта", "Келвин"]
var frequency_list = ["Герц", "Килогерц", "Мегагерц", "Гигагерц"]
var energy_list = ["Джоуль", "Килоджоуль", "Грамм-калория", "Килокалория", "Ватт-час", "Киловатт-час", "Электронвольт", "Фут-Фунт"]


ctgr.addEventListener("change", changer_of_select);

function filler(dictionary) {
  while (from.options.length) {
    from.options[0] = null;
    to.options[0] = null;
  }
  for (let i = 0; i < dictionary.length; i++) { 
    from.options[from.options.length] = new Option(dictionary[i], dictionary[i].toString);
    to.options[to.options.length] = new Option(dictionary[i], dictionary[i].toString);
  }
}
function changer_of_select(){
  switch (ctgr.value) {
    case "time":
      filler(time_list);
      break;
    case "pressure":
      filler(pressure_list);
      break;
    case "lenght":
      filler(lenght_list);
      break;
    case "mass":
      filler(mass_list);
      break;
    case "volume":
      filler(volume_list);
      break;
    case "information_volume":
      filler(inf_volume_list);
      break;
    case "angle":
      filler(angle_list);
      break;
    case "square":
      filler(square_list);
      break;
    case "speed":
      filler(speed_list)
      break;
    case "speed_inf":
      filler(speed_inf_list);
      break;
    case "temperature":
      filler(temperature_list);
      break;
    case "frequency":
      filler(frequency_list);
      break;
    case "energy":
      filler(energy_list);
      break;
    default: break;
  }
};

function alertu(){
  alert('1232')
}