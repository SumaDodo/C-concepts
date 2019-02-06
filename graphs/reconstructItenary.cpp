class Solution {
public:
    vector<string> findItinerary(vector<pair<string, string>> tickets) {
        for(auto ticket: tickets){
            targets[ticket.first].insert(ticket.second);
        }
        main_route("JFK");
        return vector<string>(route.rbegin(), route.rend());
    }
    
    map<string, multiset<string>> targets;
    vector<string> route;
    
    void main_route(string start){
        while(targets[start].size()){
            string next = *targets[start].begin();
            targets[start].erase(targets[start].begin());
            main_route(next);
        }
        route.push_back(start);
    }
};
