# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

pkgbase=ros2-jazzy-navigation2
pkgname=(
    'ros2-jazzy-costmap_queue'
    'ros2-jazzy-dwb_core'
    'ros2-jazzy-dwb_critics'
    'ros2-jazzy-dwb_msgs'
    'ros2-jazzy-dwb_plugins'
    'ros2-jazzy-nav2_amcl'
    'ros2-jazzy-nav2_behavior_tree'
    'ros2-jazzy-nav2_behaviors'
    'ros2-jazzy-nav2_bringup'
    'ros2-jazzy-nav2_bt_navigator'
    'ros2-jazzy-nav2_collision_monitor'
    'ros2-jazzy-nav2_common'
    'ros2-jazzy-nav2_constrained_smoother'
    'ros2-jazzy-nav2_controller'
    'ros2-jazzy-nav2_core'
    'ros2-jazzy-nav2_costmap_2d'
    'ros2-jazzy-nav2_dwb_controller'
    'ros2-jazzy-nav2_graceful_controller'
    'ros2-jazzy-nav2_lifecycle_manager'
    'ros2-jazzy-nav2_loopback_sim'
    'ros2-jazzy-nav2_map_server'
    'ros2-jazzy-nav2_mppi_controller'
    'ros2-jazzy-nav2_msgs'
    'ros2-jazzy-nav2_navfn_planner'
    'ros2-jazzy-nav2_planner'
    'ros2-jazzy-nav2_regulated_pure_pursuit_controller'
    'ros2-jazzy-nav2_rotation_shim_controller'
    'ros2-jazzy-nav2_route'
    'ros2-jazzy-nav2_rviz_plugins'
    'ros2-jazzy-nav2_simple_commander'
    'ros2-jazzy-nav2_smac_planner'
    'ros2-jazzy-nav2_smoother'
    'ros2-jazzy-nav2_system_tests'
    'ros2-jazzy-nav2_theta_star_planner'
    'ros2-jazzy-nav2_util'
    'ros2-jazzy-nav2_velocity_smoother'
    'ros2-jazzy-nav2_voxel_grid'
    'ros2-jazzy-nav2_waypoint_follower'
    'ros2-jazzy-nav_2d_msgs'
    'ros2-jazzy-nav_2d_utils'
    'ros2-jazzy-navigation2'
    'ros2-jazzy-opennav_docking'
    'ros2-jazzy-opennav_docking_bt'
    'ros2-jazzy-opennav_docking_core'
    'ros2-jazzy-opennav_following'
)
pkgver=1.3.13
pkgrel=1
pkgdesc="Navigation2 framework for ROS 2 Jazzy"
url="https://github.com/ros-navigation/navigation2"
arch=('x86_64')
license=('Apache-2.0')
depends=('ros2-jazzy')
makedepends=(
    'cmake'
    'licenses'
    'python-colcon-common-extensions'
    'benchmark'
    'ceres-solver'
    'eigen'
    'graphicsmagick'
    'nanoflann'
    'nlohmann-json'
    'ompl'
    'openmp'
    'python-yaml'
    'qt5-base'
    'ros2-jazzy-angles'
    'ros2-jazzy-backward_ros'
    'ros2-jazzy-behaviortree_cpp'
    'ros2-jazzy-bond'
    'ros2-jazzy-bondcpp'
    'ros2-jazzy-cv_bridge'
    'ros2-jazzy-diagnostic_updater'
    'ros2-jazzy-geographic_msgs'
    'ros2-jazzy-nav2_minimal_tb3_sim'
    'ros2-jazzy-robot_localization'
    'xsimd'
    'xtensor'
    'xtl'
)
source=("$pkgbase-$pkgver.tar.gz::https://github.com/ros-navigation/navigation2/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('424bf5ebe912156448a13c1f4153105d302fcb0a5577e9575af6007306da2670')

_srcname="navigation2-$pkgver"

prepare() {
    sed -n '2,32p' "$_srcname/nav2_dwb_controller/dwb_core/include/dwb_core/exceptions.hpp" | \
        sed 's/^ *\* *//' > "$srcdir/LICENSE.BSD-3-Clause"
    sed -i '/  ~Circle();/a\
  using Polygon::updatePolygon;' \
        "$_srcname/nav2_collision_monitor/include/nav2_collision_monitor/circle.hpp"
    find "$_srcname/nav2_mppi_controller" -type f \( -name '*.hpp' -o -name '*.cpp' \) -exec sed -i \
        -e 's#<xtensor/xtensor.hpp>#<xtensor/containers/xtensor.hpp>#g' \
        -e 's#<xtensor/xarray.hpp>#<xtensor/containers/xarray.hpp>#g' \
        -e 's#<xtensor/xrandom.hpp>#<xtensor/generators/xrandom.hpp>#g' \
        -e 's#<xtensor/xio.hpp>#<xtensor/io/xio.hpp>#g' \
        -e 's#<xtensor/xview.hpp>#<xtensor/views/xview.hpp>#g' \
        -e 's#<xtensor/xmasked_view.hpp>#<xtensor/views/xmasked_view.hpp>#g' \
        -e 's#<xtensor/xmath.hpp>#<xtensor/core/xmath.hpp>#g' \
        -e 's#<xtensor/xnoalias.hpp>#<xtensor/core/xnoalias.hpp>#g' \
        -e 's#<xtensor/xnorm.hpp>#<xtensor/reducers/xnorm.hpp>#g' \
        -e 's#<xtensor/xsort.hpp>#<xtensor/misc/xsort.hpp>#g' {} +
    sed -i \
        -e '/      int k = i \* nx;/d' \
        -e 's/j++, k++, cmap++, cm++/j++, cmap++, cm++/g' \
        "$_srcname/nav2_navfn_planner/src/navfn.cpp"
    sed -i '/^add_library(photo_at_waypoint SHARED plugins\/photo_at_waypoint.cpp)$/a\
target_include_directories(photo_at_waypoint PRIVATE /usr/include/opencv4)\
target_link_libraries(photo_at_waypoint ${OpenCV_LIBRARIES})' \
        "$_srcname/nav2_waypoint_follower/CMakeLists.txt"
    python - <<'PY'
from pathlib import Path
path = Path("navigation2-1.3.13/nav2_mppi_controller/include/nav2_mppi_controller/motion_models.hpp")
text = path.read_text()
old = """    auto view = xt::masked_view(wz, (xt::fabs(vx) / xt::fabs(wz)) < min_turning_r_);
    view = xt::sign(wz) * xt::fabs(vx) / min_turning_r_;"""
new = """    for (std::size_t i = 0; i < wz.size(); ++i) {
      const float abs_vx = vx(i) < 0.0f ? -vx(i) : vx(i);
      const float abs_wz = wz(i) < 0.0f ? -wz(i) : wz(i);
      if (abs_wz > 0.0f && abs_vx / abs_wz < min_turning_r_) {
        wz(i) = (wz(i) < 0.0f ? -abs_vx : abs_vx) / min_turning_r_;
      }
    }"""
assert old in text
path.write_text(text.replace(old, new))
PY
}

build() {
    source /opt/ros/jazzy/setup.bash

    export CFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"
    export CXXFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase -Wno-error=null-dereference"
    export CMAKE_BUILD_PARALLEL_LEVEL=2

    cd "$srcdir/$_srcname"
    colcon build \
        --executor sequential \
        --install-base "$srcdir/install" \
        --cmake-args -DCMAKE_BUILD_TYPE=None -DBUILD_TESTING=OFF -Wno-dev
}

_install_sub() {
    local sub="$1"
    install -d "$pkgdir/opt/ros/jazzy"
    cp -a "$srcdir/install/$sub/." "$pkgdir/opt/ros/jazzy/"
    rm -f "$pkgdir/opt/ros/jazzy"/COLCON_IGNORE \
          "$pkgdir/opt/ros/jazzy"/.colcon_install_layout \
          "$pkgdir/opt/ros/jazzy"/setup.* \
          "$pkgdir/opt/ros/jazzy"/local_setup.* \
          "$pkgdir/opt/ros/jazzy"/_local_setup_util_*.py \
          "$pkgdir/opt/ros/jazzy"/colcon-core-package-selection* 2>/dev/null
    install -d "$pkgdir/usr/share/licenses/$pkgname"
    case "$sub" in
        nav2_amcl)
            install -Dm644 /usr/share/licenses/spdx/LGPL-2.1-or-later.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
            ;;
        nav2_mppi_controller)
            install -Dm644 "$srcdir/$_srcname/nav2_mppi_controller/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
            ;;
        nav2_costmap_2d|nav2_map_server|nav2_navfn_planner|nav2_util)
            install -Dm644 "$srcdir/$_srcname/nav2_docking/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE.Apache-2.0"
            install -Dm644 "$srcdir/LICENSE.BSD-3-Clause" "$pkgdir/usr/share/licenses/$pkgname/LICENSE.BSD-3-Clause"
            ;;
        costmap_queue|dwb_core|dwb_critics|dwb_msgs|dwb_plugins|nav_2d_msgs|nav_2d_utils|nav2_voxel_grid)
            install -Dm644 "$srcdir/LICENSE.BSD-3-Clause" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
            ;;
        *)
            install -Dm644 "$srcdir/$_srcname/nav2_docking/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
            ;;
    esac
}

package_ros2-jazzy-costmap_queue() {
    license=('BSD-3-Clause')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_costmap_2d'
        'ros2-jazzy-nav2_common'
    )
    _install_sub costmap_queue
}

package_ros2-jazzy-dwb_core() {
    license=('BSD-3-Clause')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-dwb_msgs'
        'ros2-jazzy-nav2_costmap_2d'
        'ros2-jazzy-nav_2d_utils'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_core'
        'ros2-jazzy-nav2_common'
        'ros2-jazzy-nav_2d_msgs'
    )
    _install_sub dwb_core
}

package_ros2-jazzy-dwb_critics() {
    license=('BSD-3-Clause')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-angles'
        'ros2-jazzy-nav2_costmap_2d'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-costmap_queue'
        'ros2-jazzy-dwb_core'
        'ros2-jazzy-nav_2d_msgs'
        'ros2-jazzy-nav_2d_utils'
        'ros2-jazzy-nav2_common'
    )
    _install_sub dwb_critics
}

package_ros2-jazzy-dwb_msgs() {
    license=('BSD-3-Clause')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav_2d_msgs'
    )
    _install_sub dwb_msgs
}

package_ros2-jazzy-dwb_plugins() {
    license=('BSD-3-Clause')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-angles'
        'ros2-jazzy-dwb_core'
        'ros2-jazzy-nav_2d_msgs'
        'ros2-jazzy-nav_2d_utils'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_common'
    )
    _install_sub dwb_plugins
}

package_ros2-jazzy-nav2_amcl() {
    license=('LGPL-2.1-or-later')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav2_common'
    )
    _install_sub nav2_amcl
}

package_ros2-jazzy-nav2_behavior_tree() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-behaviortree_cpp'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_common'
    )
    _install_sub nav2_behavior_tree
}

package_ros2-jazzy-nav2_behaviors() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_behavior_tree'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav2_costmap_2d'
        'ros2-jazzy-nav2_core'
        'ros2-jazzy-nav2_common'
    )
    _install_sub nav2_behaviors
}

package_ros2-jazzy-nav2_bringup() {
    arch=('any')
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-diff_drive_controller'
        'ros2-jazzy-joint_state_broadcaster'
        'ros2-jazzy-navigation2'
        'ros2-jazzy-nav2_common'
        'ros2-jazzy-ros_gz_bridge'
        'ros2-jazzy-ros_gz_sim'
        'ros2-jazzy-slam_toolbox'
        'ros2-jazzy-xacro'
        'ros2-jazzy-nav2_minimal_tb4_sim'
        'ros2-jazzy-nav2_minimal_tb3_sim'
    )
    _install_sub nav2_bringup
}

package_ros2-jazzy-nav2_bt_navigator() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-behaviortree_cpp'
        'ros2-jazzy-nav2_behavior_tree'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_core'
        'ros2-jazzy-nav2_common'
    )
    _install_sub nav2_bt_navigator
}

package_ros2-jazzy-nav2_collision_monitor() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_common'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_costmap_2d'
        'ros2-jazzy-nav2_msgs'
    )
    _install_sub nav2_collision_monitor
}

package_ros2-jazzy-nav2_common() {
    arch=('any')
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'python-yaml'
    )
    _install_sub nav2_common
}

package_ros2-jazzy-nav2_constrained_smoother() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_common'
        'ros2-jazzy-angles'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav2_costmap_2d'
        'ros2-jazzy-nav2_core'
        'ceres-solver'
    )
    _install_sub nav2_constrained_smoother
}

package_ros2-jazzy-nav2_controller() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-angles'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav_2d_utils'
        'ros2-jazzy-nav2_costmap_2d'
        'ros2-jazzy-nav_2d_msgs'
        'ros2-jazzy-nav2_core'
        'ros2-jazzy-nav2_common'
    )
    _install_sub nav2_controller
}

package_ros2-jazzy-nav2_core() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_costmap_2d'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_behavior_tree'
        'ros2-jazzy-nav2_common'
    )
    _install_sub nav2_core
}

package_ros2-jazzy-nav2_costmap_2d() {
    license=('BSD-3-Clause' 'Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_voxel_grid'
        'ros2-jazzy-angles'
        'ros2-jazzy-nav2_common'
    )
    _install_sub nav2_costmap_2d
}

package_ros2-jazzy-nav2_dwb_controller() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-costmap_queue'
        'ros2-jazzy-dwb_core'
        'ros2-jazzy-dwb_critics'
        'ros2-jazzy-dwb_msgs'
        'ros2-jazzy-dwb_plugins'
        'ros2-jazzy-nav_2d_msgs'
        'ros2-jazzy-nav_2d_utils'
    )
    _install_sub nav2_dwb_controller
}

package_ros2-jazzy-nav2_graceful_controller() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_common'
        'ros2-jazzy-nav2_core'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_costmap_2d'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav_2d_utils'
        'ros2-jazzy-angles'
    )
    _install_sub nav2_graceful_controller
}

package_ros2-jazzy-nav2_lifecycle_manager() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-bondcpp'
        'ros2-jazzy-diagnostic_updater'
        'ros2-jazzy-nav2_common'
    )
    _install_sub nav2_lifecycle_manager
}

package_ros2-jazzy-nav2_loopback_sim() {
    arch=('any')
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_simple_commander'
        'python-transforms3d'
        'ros2-jazzy-tf_transformations'
    )
    _install_sub nav2_loopback_sim
}

package_ros2-jazzy-nav2_map_server() {
    license=('Apache-2.0' 'BSD-3-Clause')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav2_util'
        'graphicsmagick'
        'ros2-jazzy-nav2_common'
    )
    _install_sub nav2_map_server
}

package_ros2-jazzy-nav2_mppi_controller() {
    license=('MIT')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_common'
        'ros2-jazzy-nav2_core'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_costmap_2d'
        'ros2-jazzy-nav2_msgs'
        'xtensor'
        'openmp'
        'benchmark'
        'xsimd'
    )
    _install_sub nav2_mppi_controller
}

package_ros2-jazzy-nav2_msgs() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-geographic_msgs'
        'ros2-jazzy-nav2_common'
    )
    _install_sub nav2_msgs
}

package_ros2-jazzy-nav2_navfn_planner() {
    license=('Apache-2.0' 'BSD-3-Clause')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav2_common'
        'ros2-jazzy-nav2_costmap_2d'
        'ros2-jazzy-nav2_core'
    )
    _install_sub nav2_navfn_planner
}

package_ros2-jazzy-nav2_planner() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav2_common'
        'ros2-jazzy-nav2_costmap_2d'
        'ros2-jazzy-nav2_core'
    )
    _install_sub nav2_planner
}

package_ros2-jazzy-nav2_regulated_pure_pursuit_controller() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-angles'
        'ros2-jazzy-nav2_common'
        'ros2-jazzy-nav2_core'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_costmap_2d'
        'ros2-jazzy-nav2_msgs'
    )
    _install_sub nav2_regulated_pure_pursuit_controller
}

package_ros2-jazzy-nav2_rotation_shim_controller() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_common'
        'ros2-jazzy-nav2_core'
        'ros2-jazzy-nav2_controller'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_costmap_2d'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-angles'
    )
    _install_sub nav2_rotation_shim_controller
}

package_ros2-jazzy-nav2_route() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-nav2_costmap_2d'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_core'
        'ros2-jazzy-angles'
        'nanoflann'
        'nlohmann-json'
        'ros2-jazzy-nav2_common'
    )
    _install_sub nav2_route
}

package_ros2-jazzy-nav2_rviz_plugins() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_lifecycle_manager'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav2_route'
        'qt5-base'
    )
    _install_sub nav2_rviz_plugins
}

package_ros2-jazzy-nav2_simple_commander() {
    arch=('any')
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_msgs'
    )
    _install_sub nav2_simple_commander
}

package_ros2-jazzy-nav2_smac_planner() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav2_common'
        'ros2-jazzy-nav2_costmap_2d'
        'ros2-jazzy-nav2_core'
        'eigen'
        'ompl'
        'nlohmann-json'
        'ros2-jazzy-angles'
    )
    _install_sub nav2_smac_planner
}

package_ros2-jazzy-nav2_smoother() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-angles'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav_2d_utils'
        'ros2-jazzy-nav_2d_msgs'
        'ros2-jazzy-nav2_core'
        'ros2-jazzy-nav2_common'
    )
    _install_sub nav2_smoother
}

package_ros2-jazzy-nav2_system_tests() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_bringup'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_map_server'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav2_lifecycle_manager'
        'ros2-jazzy-nav2_navfn_planner'
        'ros2-jazzy-nav2_behavior_tree'
        'ros2-jazzy-nav2_amcl'
        'ros2-jazzy-nav2_minimal_tb3_sim'
        'ros2-jazzy-navigation2'
        'lcov'
        'ros2-jazzy-nav2_planner'
        'ros2-jazzy-nav2_common'
    )
    _install_sub nav2_system_tests
}

package_ros2-jazzy-nav2_theta_star_planner() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_common'
        'ros2-jazzy-nav2_core'
        'ros2-jazzy-nav2_costmap_2d'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav2_util'
    )
    _install_sub nav2_theta_star_planner
}

package_ros2-jazzy-nav2_util() {
    license=('Apache-2.0' 'BSD-3-Clause')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_common'
        'ros2-jazzy-bond'
        'ros2-jazzy-bondcpp'
        'ros2-jazzy-nav2_msgs'
    )
    _install_sub nav2_util
}

package_ros2-jazzy-nav2_velocity_smoother() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_common'
    )
    _install_sub nav2_velocity_smoother
}

package_ros2-jazzy-nav2_voxel_grid() {
    license=('BSD-3-Clause')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_common'
    )
    _install_sub nav2_voxel_grid
}

package_ros2-jazzy-nav2_waypoint_follower() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_common'
        'ros2-jazzy-cv_bridge'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_core'
        'ros2-jazzy-robot_localization'
        'ros2-jazzy-geographic_msgs'
    )
    _install_sub nav2_waypoint_follower
}

package_ros2-jazzy-nav_2d_msgs() {
    license=('BSD-3-Clause')
    depends=(
        'ros2-jazzy'
    )
    _install_sub nav_2d_msgs
}

package_ros2-jazzy-nav_2d_utils() {
    license=('BSD-3-Clause')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav_2d_msgs'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_common'
    )
    _install_sub nav_2d_utils
}

package_ros2-jazzy-navigation2() {
    arch=('any')
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_amcl'
        'ros2-jazzy-nav2_behavior_tree'
        'ros2-jazzy-nav2_bt_navigator'
        'ros2-jazzy-nav2_collision_monitor'
        'ros2-jazzy-nav2_constrained_smoother'
        'ros2-jazzy-nav2_controller'
        'ros2-jazzy-nav2_core'
        'ros2-jazzy-nav2_costmap_2d'
        'ros2-jazzy-nav2_dwb_controller'
        'ros2-jazzy-nav2_graceful_controller'
        'ros2-jazzy-nav2_lifecycle_manager'
        'ros2-jazzy-nav2_map_server'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav2_mppi_controller'
        'ros2-jazzy-nav2_navfn_planner'
        'ros2-jazzy-nav2_planner'
        'ros2-jazzy-nav2_behaviors'
        'ros2-jazzy-nav2_smoother'
        'ros2-jazzy-nav2_regulated_pure_pursuit_controller'
        'ros2-jazzy-nav2_route'
        'ros2-jazzy-nav2_rotation_shim_controller'
        'ros2-jazzy-nav2_rviz_plugins'
        'ros2-jazzy-nav2_simple_commander'
        'ros2-jazzy-nav2_smac_planner'
        'ros2-jazzy-nav2_theta_star_planner'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_velocity_smoother'
        'ros2-jazzy-nav2_voxel_grid'
        'ros2-jazzy-nav2_waypoint_follower'
        'ros2-jazzy-opennav_docking'
        'ros2-jazzy-opennav_docking_bt'
        'ros2-jazzy-opennav_docking_core'
    )
    _install_sub navigation2
}

package_ros2-jazzy-opennav_docking() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-angles'
        'ros2-jazzy-nav2_graceful_controller'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-opennav_docking_core'
    )
    _install_sub opennav_docking
}

package_ros2-jazzy-opennav_docking_bt() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_behavior_tree'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_core'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-behaviortree_cpp'
    )
    _install_sub opennav_docking_bt
}

package_ros2-jazzy-opennav_docking_core() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-nav2_msgs'
    )
    _install_sub opennav_docking_core
}

package_ros2-jazzy-opennav_following() {
    license=('Apache-2.0')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_msgs'
        'ros2-jazzy-nav2_util'
        'ros2-jazzy-opennav_docking'
        'ros2-jazzy-opennav_docking_core'
        'ros2-jazzy-nav2_common'
        'ros2-jazzy-angles'
    )
    _install_sub opennav_following
}
