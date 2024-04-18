#include <iostream>
#include <vector>
#include <wykobi/wykobi.hpp>
#include <wykobi/wykobi_utilities.hpp>
#include <wykobi/wykobi_algorithm.hpp>

namespace wy = wykobi;
namespace alg = wykobi::algorithm;

int main(void) {

  typedef long double LD;

  wy::point2d<LD> point1 = wy::make_point(0.0L, 0.0L);
  wy::point2d<LD> point2 = wy::make_point(1.0L, 0.0L);

  wy::circle<LD> c1 = wy::make_circle(0.0L, 0.0L, 1.0L);
  wy::circle<LD> c2 = wy::make_circle(1.0L, 0.0L, 1.0L);
  std::vector<wy::circle<LD>> circles = {c1, c2};
  std::vector<wy::point2d<LD>> inter;
  alg::naive_group_intersections<wy::circle<LD>>(circles.begin(), circles.end(),
                                                std::back_inserter(inter));
  for (auto p : inter) {
    std::cout << p << " ";
  }

  std::cout << "\n";
  return 0;
}
