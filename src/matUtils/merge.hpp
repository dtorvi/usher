#include "common.hpp"
typedef tbb::concurrent_hash_map<MAT::Node*, MAT::Node*> concurMap;
po::variables_map parse_summary_command(po::parsed_options parsed);
bool consistent(MAT::Tree T, MAT::Tree B);
bool chelper(MAT::Node* a, MAT::Node* b);
void merge_main(po::parsed_options parsed);
extern concurMap consistNodes;
std::vector<std::string> mainhelper(std::vector<std::string> samples,  MAT::Tree finalMat,  MAT::Tree baseMat,  MAT::Tree otherMat);
