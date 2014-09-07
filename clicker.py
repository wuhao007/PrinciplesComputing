"""
Cookie Clicker Simulator
"""
 
import simpleplot
import math
 
# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)
 
import poc_clicker_provided as provided
 
# Constants
SIM_TIME = 10000000000.0
 
class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._total_cookies = 0.0
        self._current_cookies = 0.0
        self._current_time = 0.0
        self._current_cookies_per_second = 1.0
        self._history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        return "Time: " + str(self._current_time) + "\nCurrent Cookies: " + str(self._current_cookies) + "\nCPS: " + str(self._current_cookies_per_second) + "\nTotal Cookies: " + str(self._total_cookies) + "\n" + str(self._history)
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS
 
        Should return a float
        """
        return self._current_cookies_per_second
    
    def get_time(self):
        """
        Get current time
 
        Should return a float
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list
 
        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)
 
        For example: (0.0, None, 0.0, 0.0)
        """
        return self._history
 
    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0 if you already have enough cookies)
 
        Should return a float with no fractional part
        """
        # Galletas que necesito es DIFF = Galletas que cuesta [-] mis galletas actuales
        # ej. Necesito (cookies = 150) 150 galletas y actualmente tengo 200 (current_cookies = 200), DIFF = -50
        # diff = -50 <= 0 ? SI entonces regresa 0 porque no necesito esperar nada de tiempo.
        #
        # Caso contrario:
        #            Necesito 150 galletas y actualmente solo tengo 100, 150 - 100 = 50
        #            diff = 50 <= 0 ? NO, entonces  math.ceil(50 / 1.0) = 50 
        diff =  cookies - self._current_cookies
        
        if(diff <= 0):
            return 0.0
        else:
            return math.ceil(diff / self._current_cookies_per_second)
    
    def wait(self, time):
        """
        Wait for given amount of time and update state
 
        Should do nothing if time <= 0
        """
        # wait() allows you to jump in time to the moment you have enough cookies to purchase an upgrade
        # - the state of your game does nothing in between purchases, but accumulate cookies; 
        # wait() compresses time by multiplying time_until() by the cps to calculate the number of cookies baked during that time.
 
        if(time <= 0):
            return
        else:
            self._current_time = float(self.get_time()) + time
            self._current_cookies = self.get_cookies() + (self.get_cps() * time)
            self._total_cookies = self._total_cookies + (self.get_cps() * time)
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state
 
        Should do nothing if you cannot afford the item
        """
        # Si el costo es menor o igual a mi numero actual de galletas, lo puedo comprar
        # De mi número actual de galletas le quito lo que me costó comprar el objeto
        # Mi galletas por segundo se ven aumentadas por la mejorar que acabo de comprar, agregar los cps que me da la mejora
        # Agregar al historial la mejora
        if cost <= self.get_cookies():
            self._current_cookies =  self._current_cookies - cost
            self._current_cookies_per_second = self._current_cookies_per_second + additional_cps
            self._history.append((self._current_time, item_name, cost, self._total_cookies))
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to game.
    """
    # Replace with your code
 
    clicker = ClickerState()
    new_build_info = build_info.clone()
    stop = False
 
    while ((clicker.get_time() <= duration) and (not stop)):
        
        item = strategy(clicker.get_cookies(), 
                             clicker.get_cps(), 
                             duration - clicker.get_time(), 
                             new_build_info)
 
        if(item == None):
            clicker.wait(duration - clicker.get_time())
            stop = True
            
        else:
            # ¿Se puede comprar el item con las galletas actuales?
            #Si
            costo_item = new_build_info.get_cost(item)
            cps_item = new_build_info.get_cps(item)
 
            if (clicker.get_cookies() >= costo_item):
                
                clicker.buy_item(item, costo_item, cps_item)
                new_build_info.update_item(item)
                
            # No, entonces ir al tiempo en el cual ya tengo suficientes
            # galletas para comprar la mejora, sin pasar el tiempo de simulación.
            
            else:
                elapsed_time = clicker.time_until(new_build_info.get_cost(item))
 
                if elapsed_time > (duration - clicker.get_time()):
                    clicker.wait(duration - clicker.get_time())
                    stop = True
                else:
                    clicker.wait(elapsed_time)
                    clicker.buy_item(item, costo_item, cps_item)
                    new_build_info.update_item(item)
    return clicker
 
def strategy_cursor(cookies, cps, time_left, build_info):
    """
    Always pick Cursor!
 
    Note that this simplistic strategy does not properly check whether
    it can actually buy a Cursor in the time left.  Your strategy
    functions must do this and return None rather than an item you
    can't buy in the time left.
    """
    return "Cursor"
 
def strategy_none(cookies, cps, time_left, build_info):
    """
    Always return None
 
    This is a pointless strategy that you can use to help debug
    your simulate_clicker function.
    """
    return None
 
def strategy_cheap(cookies, cps, time_left, build_info):
    """
    Return human readable state
    """
    build_list = build_info.build_items()
    cheapest_option = build_list[0]
    total_cookies = cookies + (cps * time_left)
 
    for build_option in build_list:
        if build_info.get_cost(build_option) < build_info.get_cost(cheapest_option):
            cheapest_option = build_option
 
    if build_info.get_cost(cheapest_option) > total_cookies:
        return None
 
    return cheapest_option
 
def strategy_expensive(cookies, cps, time_left, build_info):
    """
    Return human readable state
    """
    build_list = build_info.build_items()
    expensive_list = []
    selection = build_list[0]
    total_cookies = cookies + (cps * time_left)
 
    for build_option in build_list:
        if build_info.get_cost(build_option) <= total_cookies:
            expensive_list.append(build_option)
 
    if len(expensive_list) == 0:
        return None
 
    for expensive_option in expensive_list:
        if build_info.get_cost(expensive_option) > build_info.get_cost(selection):
            selection = expensive_option
 
    return selection
 
def strategy_best(cookies, cps, time_left, build_info):
    """
    Return human readable state
    """
    return None
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation with one strategy
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state
 
    # Plot total cookies over time
 
    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it
 
    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)
 
def run():
    """
    Run the simulator.
    """    
    #run_strategy("Cursor", SIM_TIME, strategy_cursor)
    
    # Mis pruebas
    #run_strategy("Cursor", 5000, strategy_none)
    #run_strategy("Cursor", 10, strategy_cursor)
    #run_strategy("Cursor", 16, strategy_cursor)
 
    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)
    
run()
#print simulate_clicker(provided.BuildInfo({'Cursor': [15.0, 50.0]}, 1.15), 16, strategy_cursor)
#obj = ClickerState()
#obj.wait(402)
#obj.buy_item('item', 2.0, 9.0)
#print obj.time_until(49)
#print obj._history